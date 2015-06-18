

function get_github_info() {

        $.ajax({
            url: "https://api.github.com/repos/" + $("#repo_name").val(),
            dataType: 'jsonp',
            jsonp: 'callback',
            jsonpCallback: 'jsonpCallback',
            success: function(){
                alert("success");
            }
        });


};
