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

    // Get date one month ago, in ISO format, for "in the last month" queries.
    date = new Date();
    date.setMonth(date.getMonth() - 1);
    last_month_iso = date.toISOString();

    makeCorsRequest("https://api.github.com/repos/" + data.full_name + "/commits?since=" + last_month_iso + "&per_page=300", parse_commits);
    makeCorsRequest("https://api.github.com/repos/" + data.full_name + "/contributors", parse_contribs);
    makeCorsRequest("https://api.github.com/repos/" + data.full_name + "/issues?state=all&per_page=100", parse_issues);
    makeCorsRequest("https://api.github.com/repos/" + data.full_name + "/pulls?state=all&per_page=100", parse_prs);

}

function parse_commits(xhr) {

    if (xhr.status == 200) {

        var data = jQuery.parseJSON(xhr.responseText);
        if(data.length == 300){
            commits = "300 or more;"
        } else {
            commits = data.length;
        }

        $("#checklist_commits").text("There have been " + commits + " commits in the last month.");
    } else {
        $("#checklist_commits").text("There was an error.");
    };

}

function parse_contribs(xhr) {

    if (xhr.status == 200) {
        var data = jQuery.parseJSON(xhr.responseText);
        $("#checklist_contribs").text("There are " + data.length + " contributors to this repository.");
    } else {
        $("#checklist_contribs").text("There was an error.");
    };

}

function parse_issues(xhr) {

    if (xhr.status == 200) {

        var data = jQuery.parseJSON(xhr.responseText);

        comments = [];
        replied_count = 0;

        for (var i = 0; i < data.length; i++) {
            if(!data[i].hasOwnProperty('pull_request')) {
                comments.push(data[i].comments);
                if(data[i].comments != 0) {
                    replied_count += 1;
                }
            }
        };

        comment_percent = parseInt((replied_count / comments.length) * 100);

        $("#checklist_issues").text(comment_percent + "% of " + comments.length +
            " issues get replies. The median number of replies is " +
            math.median(comments) + ".");

    } else {
        $("#checklist_issues").text("There was an error.");
    };

}

function parse_prs(xhr) {

    if (xhr.status == 200) {

        var data = jQuery.parseJSON(xhr.responseText);

        var pr_merged = 0;

        for (var i = 0; i < data.length; i++) {
            if(data[i].merged_at != null) {
                pr_merged += 1;
            };
        };

        pr_percent = parseInt((pr_merged / data.length) * 100);

        $("#checklist_mergedprs").text(pr_percent + "% of " + data.length + " pull requests have been merged.");

    } else {
        $("#checklist_mergedprs").text("There was an error.");
    };

}
