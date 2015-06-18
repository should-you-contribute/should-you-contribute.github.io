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
            if (this.status == 200) { // If the HTTP response code is 200 (e.g. successful)
                // Response handlers.
                console.log(xhr.responseText);
            };
        };
    };

    xhr.onerror = function() {
        alert('Woops, there was an error making the request.');
    };

    xhr.send();
}
