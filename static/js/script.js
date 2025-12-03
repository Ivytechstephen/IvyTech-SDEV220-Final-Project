$(document).ready(function() {

    // Handle "Use Template"
    $('.use-template-btn').click(function() {
        const templateId = $(this).data('id');
        
        $.post(`/use_template/${templateId}`, function(data) {
            if(data.success) {
                location.reload(); // Reload to show the new list
            }
        });
    });

    // Handle "Save as Template"
    $('.save-template-btn').click(function() {
        const listId = $(this).data('id');
        
        $.post(`/save_as_template/${listId}`, function(data) {
            if(data.success) {
                alert('Template Saved!');
                location.reload();
            }
        });
    });

});
