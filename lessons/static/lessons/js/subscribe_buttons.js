/**
 * Controls visibility of subscribe, unsubscribe and start lesson
 * buttons through ajax
*/
 
function subscribe(subscribe, lesson_id) {
    $.ajax({
        alert('clicked');
        type:"GET",
        url:"/lessons/subscriptions",
        data:{  
                subscribe: subscribe,
                lesson_id: lesson_id,
            },
        success: function(json_response){
            if (json_response['subscription_status'] == 'unsubscribed') {
                // Unsub button
                $('#unsubscribe_lesson_button_id_'+lesson_id).hide();
                // Sub button
                $('#subscribe_lesson_button_id_'+lesson_id).removeAttr('hidden');
                $('#subscribe_lesson_button_id_'+lesson_id).show();
                // Start Lesson button
                $('#start_lesson_button_id_'+lesson_id).hide();
            } else if (json_response['subscription_status'] == 'subscribed') {
                // Unsub button
                $('#unsubscribe_lesson_button_id_'+lesson_id).removeAttr('hidden');
                $('#unsubscribe_lesson_button_id_'+lesson_id).show();
                // Sub button
                $('#subscribe_lesson_button_id_'+lesson_id).hide();
                // Start Lesson button
                $('#start_lesson_button_id_'+lesson_id).removeAttr('hidden');
                $('#start_lesson_button_id_'+lesson_id).show();
            }
        }
    })
}
