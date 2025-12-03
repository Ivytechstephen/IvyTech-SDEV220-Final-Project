from flask import Flask, render_template, request, jsonify, redirect, session, flash, url_for
from flask_session import Session
from models import User, List_Obj, Item_Obj, Profanity, db

from sqlalchemy import or_
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required
import datetime


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Setup Webapp
@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

#----------------------Functions to check username, password, and profanity----------------------

# Function to check if username meets criteria
def check_username(username):
    if len(username) < 8 or len(username) > 16:
        return False
    return True


# Function to check if Input is Clean NO PROFANITY
def check_profanity(input_text):
    # Split by whitespace 
    words = input_text.split() 

    for word in words:
        word_clean = word.lower()
        
        # Use SQLAlchemy to check if the word exists in any of the 4 columns
        exists = Profanity.query.filter(
            or_(
                Profanity.word == word_clean,
                Profanity.canonical_form_1 == word_clean,
                Profanity.canonical_form_2 == word_clean,
                Profanity.canonical_form_3 == word_clean
            )
        ).first()

        
        # If a match is not found, exists will return False .
        if exists:
            return False
        
    # If a match is found, exists will return True 
    return True


# Function to check if password meets criteria
def check_password(password):
    l, u, d, s = 0, 0, 0, 0
    special = ["!", "@", "#", "$", "%", "&", "*", "_", ".", "?"]
    if len(password) >= 8 or len(password) <= 32:
        for i in password:
            if i.islower():
                l += 1
            if i.isupper():
                u += 1
            if i.isdigit():
                d += 1
            if i in special:
                s += 1
        if l >= 1 and u >= 1 and d >= 1 and s >= 1: 
            return True
        else:
            return False
    else:
        return False
#------------------------------------- End of functions ---------------------------------------


#----------------------------------------- Routes ---------------------------------------------


# Registration route
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Validation Checks
        if not username:
            return apology("Please enter a username.", 400)
        
        if check_username(username) == False:
            flash("Username must be at least 8 characters long.")
            return redirect("/register")

        if check_profanity(username) == False:
            flash("Please enter a Username without Profanities.")
            return redirect("/register")
        
        # Check for Existing User 
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return apology("Sorry this Username is already taken.", 400)

        # Password Checks
        if not password or not confirmation:
            return apology("Please enter the password in both boxes.", 400)

        if password != confirmation:
            return apology("Passwords do not match.", 400)

        if check_password(password) == False:
            flash("Password must contain 1 Lowercase, 1 Uppercase, 1 Number, and 1 Special Character.")
            return redirect("/register")

        # Create and Save User
        hashed = generate_password_hash(password)
        
        # Create new instance of User class
        new_user = User(username=username, hash=hashed)
        
        # Add to session and commit
        db.session.add(new_user)
        db.session.commit()

        flash("Successfully registered as " + username)
        return render_template("login.html")

    else:
        return render_template("register.html")



@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # If User reached route via POST.
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Ensure username was submitted.
        if not username:
            return apology("must provide username", 403)

        # Ensure password was submitted.
        elif not password:
            return apology("must provide password", 403)

        # Query database for username using SQLAlchemy
        user = User.query.filter_by(username=username).first()

        # Ensure username exists and password is correct
        if not user or not check_password_hash(user.hash, password):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = user.id

        # Flash message.
        flash("Welcome")

        # Redirect user to home page.
        return redirect("/")

    # Else User reached route via GET.
    else:
        return render_template("login.html")



@app.route("/logout")
@login_required
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Flash message
    flash("Logged Out")

    # Redirect user to login form
    return redirect("/")


# Index route (Main Page)
@app.route('/')
@login_required
def index():
    current_user_id = session["user_id"] 

    active_lists = List_Obj.query.filter_by(is_template=False, user_id=current_user_id).all()
    templates = List_Obj.query.filter_by(is_template=True, user_id=current_user_id).all()
    return render_template('index.html', lists=active_lists, templates=templates)


# Create List route 
@app.route('/create_list', methods=['POST'])
@login_required
def create_list():
    list_name = request.form.get("list_name")
    
    # Create the new list
    new_list = List_Obj(
        name=list_name,
        is_template=False,
        user_id=session["user_id"]
    )
    db.session.add(new_list)
    db.session.commit()
    
    # Redirect directly to the NEW list's page using the list.id
    return redirect(url_for('view_list', list_id=new_list.id))


# View a Specific List
@app.route('/lists/<int:list_id>', methods=['GET'])
@login_required
def view_list(list_id):
    list_to_view = List_Obj.query.get_or_404(list_id)
    if list_to_view.user_id != session["user_id"]:
        return apology("Abort", 403)
    return render_template('view_list.html', current_list=list_to_view)


# Add a single Item to the List 
@app.route('/add_item/<int:list_id>', methods=['POST'])
@login_required
def add_item(list_id):
    content = request.form.get("content")
    
    if content:
        new_item = Item_Obj(
            content=content,
            # Defaults to 1
            quantity=1, 
            is_completed=False,
            list_id=list_id
        )
        db.session.add(new_item)
        db.session.commit()
        
    # Refresh the page by redirecting back to the view_list route
    return redirect(url_for('view_list', list_id=list_id))


# Delete Item
@app.route('/delete_item', methods=['POST'])
@login_required
def delete_item():
    item_id = request.form.get("item_id")
    # Needed for redirect
    list_id = request.form.get("list_id")
    
    item = Item_Obj.query.get_or_404(item_id)
    
    # Ensure the list belongs to the user
    parent_list = List_Obj.query.get(list_id)
    if parent_list.user_id == session["user_id"]:
        db.session.delete(item)
        db.session.commit()
    
    return redirect(url_for('view_list', list_id=list_id))


# Save existing list as a Template
@app.route('/save_as_template/<int:list_id>', methods=['POST'])
def save_as_template(list_id):
    original_list = List_Obj.query.get_or_404(list_id)
    
    # Create the Template Clone
    new_template = List_Obj(name=f"{original_list.name} (Template)", is_template=True)
    db.session.add(new_template)
    db.session.commit() # Commit to get the new ID
    
    # Deep Copy of Items from original list
    for item in original_list.items:
        new_item = Item_Obj(
            content=item.content,
            # Preserve quantity structure
            quantity=item.quantity, 
            # Reset completion status for the template
            is_completed=False,     
            list_id=new_template.id
        )
        db.session.add(new_item)
    
    db.session.commit()
    return jsonify({'success': True, 'message': 'Template saved!'})



# Create new List from Template
@app.route('/use_template/<int:template_id>', methods=['POST'])
@login_required
def use_template(template_id):
    template = List_Obj.query.get_or_404(template_id)
    
    new_list = List_Obj(
        name=f"Job from {template.name}", 
        is_template=False,
        # Assign to current user
        user_id=session["user_id"] 
    )
    db.session.add(new_list)
    db.session.commit()
    
    # Deep Copy items from Template to New List
    for item in template.items:
        new_item = Item_Obj(
            content=item.content,
            # Start with template quantities
            quantity=item.quantity, 
            is_completed=False,
            list_id=new_list.id
        )
        db.session.add(new_item)
        
    db.session.commit()

    # Debugging (REMOVE ME)
    return jsonify({'success': True, 'id': new_list.id})


# Route to Save the data to the database
@app.route('/save_new_list', methods=['POST'])
@login_required
def save_new_list():
    list_type = request.form.get("list_type")
    list_name = request.form.get("list_name")
    
    # Get lists of all item inputs
    contents = request.form.getlist("contents[]")
    quantities = request.form.getlist("quantities[]")

    # Determine if it is a template based on the hidden input
    is_template_bool = True if list_type == "template" else False

    # Create the List Object
    new_list = List_Obj(
        name=list_name,
        is_template=is_template_bool,
        user_id=session["user_id"]
    )
    db.session.add(new_list)
    # Commit to generate the new_list.id
    db.session.commit() 

    # Loop through the inputs and create Item Objects
    # zip() is used to pair the content with its corresponding quantity
    for content, quantity in zip(contents, quantities):
        # Only add if content is not empty
        if content.strip(): 
            new_item = Item_Obj(
                content=content,
                quantity=int(quantity) if quantity else 1,
                is_completed=False,
                list_id=new_list.id
            )
            db.session.add(new_item)

    db.session.commit()

    flash(f"{list_type.capitalize()} '{list_name}' created!")
    return redirect("/")


@app.route('/delete_list/<int:list_id>', methods=['POST'])
def delete_list(list_id):
    list_to_delete = List_Obj.query.get_or_404(list_id)
    
    try:
        db.session.delete(list_to_delete)
        db.session.commit()
        flash("List deleted successfully!", "success")
    except:
        flash("There was a problem deleting that list.", "error")
        
    return redirect(url_for('index'))
    
    

if __name__ == '__main__':
    app.run(debug=True)
    