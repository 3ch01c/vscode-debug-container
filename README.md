# vscode-debug-container

This is just a project to help me understand how to debug inside a container.

First, you'll need [VS Code](https://code.visualstudio.com/Download)] and
[the Docker extension](https://code.visualstudio.com/docs/containers/overview).
Next, you'll need to check out the documentation on
[how to debug containerized apps](https://code.visualstudio.com/docs/containers/debug-common).
I'm
[debugging Python](https://code.visualstudio.com/docs/containers/debug-python),
but you can do [Node](https://code.visualstudio.com/docs/containers/debug-node),
[.NET](https://code.visualstudio.com/docs/containers/debug-netcore), and others.

There's some helpers to get you going. Create a new VS Code project, open up the
Command Palette (Ctrl+Shift+P), select _Docker: Add Docker Files to Workspace_
and follow the prompts to set up a project for debugging. This creates a
`.vscode` directory with two files: `launch.json` and `tasks.json` as well as a
`Dockerfile`. You can also use the _Docker: Add Docker Compose Files to
Workspace_ to add a `docker-compose.yml` if you like.

If you're using this demo project, the app is configured with a basic network
socket connection. Once deployed, you should be able to find the host port 
using `docker ps`. Just load up `http://localhost:<PORT>` in your browser or
another program that uses network sockets and the program should end.