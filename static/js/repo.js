getRepos();
async function getRepos()
{
    const user_url = "https://api.github.com/users/araon/repos"
    const response = await fetch(user_url)
    const result = await response.json()
    result.forEach(i => {
        const anchor = document.createElement("a")
        anchor.href = i.html_url
        anchor.textContent = "Link";
        console.log(anchor)
        document.getElementById("repo_link").appendChild(anchor)
        document.getElementById("repo_link").appendChild(document.createElement("br"))
        document.getElementById("repo_name").appendChild(document.createTextNode(i.name))
        document.getElementById("repo_name").appendChild(document.createElement("br"))
        document.getElementById("repo_lang").appendChild(document.createTextNode(i.language))
        document.getElementById("repo_lang").appendChild(document.createElement("br"))
    });

}