import subprocess

import typer

def main():

    project = typer.prompt("Project name:", default="LACE")
    key = int(typer.prompt("Issue key:"))
    ticket = f"{project}-{key}"

    desc = typer.prompt("Short description:")
    desc_format = desc.replace(" ", "_").lower()
    branch_name = f"{ticket}-{desc_format}"

    base_branch = typer.prompt("Base branch:", default="master")

    title = f"{ticket} | {desc}"
    typer.echo(f"Tiket: {title}")

    subprocess.run(["git", "fetch", "origin" f"{base_branch}:{base_branch}"])
    subprocess.run(["git", "checkout", "-b", branch_name, base_branch])
    subprocess.run(["git", "push", "origin", branch_name])

    subprocess.run(["gh", "pr", "create", "-d", "--title", title, "--body", "" "--base", base_branch])


if __name__ == "__main__":
    typer.run(main)
