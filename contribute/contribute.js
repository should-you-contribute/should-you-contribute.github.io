$(document).ready(function() {

    $("#repo_submit").click(function(e) {

        e.preventDefault();
        var xhr = makeCorsRequest("https://api.github.com/repos/"
            + $("#repo_name").val(), parse_initial_request);

    });

});

function makeCorsRequest(url, callback) {

    var xhr = new XMLHttpRequest();

    if ("withCredentials" in xhr) {
        // XHR for Chrome/Firefox/Opera/Safari.
        xhr.open('GET', url, true);
    } else if (typeof XDomainRequest != "undefined") {
        // XDomainRequest for IE.
        xhr = new XDomainRequest();
        xhr.open('GET', url);
    } else {
        // CORS not supported.
        xhr = null;
    }

    if (!xhr) {
        alert('CORS not supported');
        return;
    }

    // Waits for request response before executing.
    xhr.onreadystatechange = function ( ) {
        if (this.readyState == 4) { // If the HTTP request has completed
            callback(this);
        };
    };

    xhr.onerror = function() {
        alert('Woops, there was an error making the request.');
    };

    xhr.send();

}

function parse_initial_request(xhr) {

    if (xhr.status == 404) {
        $("#repo_error").text("That is not a valid, public Github repository.  Please try again.");
    };

    if (xhr.status == 403) {
        $("#repo_error").text("Too many people are using this site.  Please try again later.");
    };

    if (xhr.status == 200) {
        $("#repo_error").text("Success!");
        parse_github_response(xhr);
    };

}

function parse_github_response(xhr) {

    var data = jQuery.parseJSON(xhr.responseText);

    // Add repo name to title
    $('#checklist_title').prepend(data.full_name + "'s ");

    makeCorsRequest("https://api.github.com/repos/" + $("#repo_name").val() + "/contributors", parse_contribs);

    console.log(data);

}

function parse_contribs(xhr) {

    if (xhr.status == 200) {
        var data = jQuery.parseJSON(xhr.responseText);
        $("#checklist_contribs").text("There are " + data.length + " contributors to this repository.");
    } else {
        $("#checklist_contribs").text("There was an error.");
    };

}
