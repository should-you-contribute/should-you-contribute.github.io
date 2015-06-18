$(document).ready(function() {

    $("#repo_submit").click(function(e) {
        e.preventDefault();
        makeCorsRequest();
    });

});


function createCORSRequest(method, url) {
    var xhr = new XMLHttpRequest();
    if ("withCredentials" in xhr) {
        // XHR for Chrome/Firefox/Opera/Safari.
        xhr.open(method, url, true);
    } else if (typeof XDomainRequest != "undefined") {
        // XDomainRequest for IE.
        xhr = new XDomainRequest();
        xhr.open(method, url);
    } else {
        // CORS not supported.
        xhr = null;
    }
    return xhr;
}

function makeCorsRequest() {

    var url = "https://api.github.com/repos/" + $("#repo_name").val();

    var xhr = createCORSRequest('GET', url);

    if (!xhr) {
        alert('CORS not supported');
        return;
    }

    // Waits for request response before executing.
    xhr.onreadystatechange = function () {
        if (this.readyState == 4) { // If the HTTP request has completed

            // 404 -- try again
            if (this.status == 404) {
                $("#repo_error").text("That is not a valid, public Github repository.  Please try again.");
            };

            // 403 -- rate limit exceeded
            if (this.status == 403) {
                $("#repo_error").text("Too many people are using this site.  Please try again later.");
            };

            // 200 -- yay parsing time
            if (this.status == 200) {
                $("#repo_error").text("Success!");
                parse_github_response(xhr);
            };
        };
    };

    xhr.onerror = function() {
        alert('Woops, there was an error making the request.');
    };

    xhr.send();
}

function parse_github_response(xhr) {

    var data = jQuery.parseJSON(xhr.responseText);

    // Add repo name to title
    $('#checklist_title').prepend(data.full_name + "'s ");

    console.log(data);

}
