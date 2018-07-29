$(document).ready(() => {
    $('.short_url_detail').click(toggleAdjustmentMenu);
    $('.btn_cancel').click((ev) => {
        ev.preventDefault();
        $('.short_url_detail').trigger('click')
    });

    function toggleAdjustmentMenu() {
        $('.adj_menu').toggle('hidden')
    }

    $('.create_url').submit(function(ev) {
        $.post("/", $('.create_url').serialize(), (data, status) => {
            if (status !== 'success') {
                alert('Url is incorrect')
            }
        })
    })

    $('.action_form').submit(function(ev) {
        ev.preventDefault();
        let updateAction = $(document.activeElement).hasClass('btn_save');
        if (updateAction) {
            $.post("/update_url/", $('.action_form').serialize(), (data, status, xhr) => {
                if (xhr.status === 200) {
                    alert('Url was succefully updated');
                    location.reload();
                }
                if (xhr.status === 203) {
                    alert(data)
                }
            })
        } else {
            $.ajax({
                url: "/update_url/",
                type: 'DELETE',
                headers: {
                    "X-CSRFToken": getCookie('csrftoken')
                },
                success: function(result, status) {
                    if (status === 'success') {
                        alert('Url was succefully deleted');
                        location.reload();
                    } else {
                        alert('Nothing to delete');
                    }
                }
            });
        }
    });

    // generate csrf token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            let cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                let cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});