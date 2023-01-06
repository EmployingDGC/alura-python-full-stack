def clean_render_template(string: str) -> str:
    return (
        string
            .replace("&lt;", "<")
            .replace("&#34;", "\"")
            .replace("&gt;", ">")
    )
