getRepos();
async function getRepos()
{
    const user_url = "https://api.github.com/users/araon/repos"
    const response = await fetch(user_url)
    const result = await response.json()
    var i;
    for (i = 0; i < result.length; i++) {
        if (result[i]['fork'] === false){
            const anchor = document.createElement("a")
            anchor.href = result[i]["html_url"]
            anchor.textContent = "Link";
            document.getElementById("repo_link").appendChild(anchor)
            document.getElementById("repo_link").appendChild(document.createElement("br"))
            document.getElementById("repo_name").appendChild(document.createTextNode(result[i]["name"]))
            document.getElementById("repo_name").appendChild(document.createElement("br"))
            document.getElementById("repo_lang").appendChild(document.createTextNode(result[i]["language"]))
            document.getElementById("repo_lang").appendChild(document.createElement("br"))
            
        }
    }
}