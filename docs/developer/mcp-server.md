# MCP Server

The accsyn MCP server lets an AI agent such as ChatGPT or Claude work with your accsyn workspace: list transfers and their files, read logs, and pause, resume or abort jobs. It runs on your own computer and uses the accsyn [JavaScript API](/developer/javascript-api/) to talk to your workspace.

*Important Note: The server uses the accsyn API, which is NOT available for Cloud Essentials or [BYOS](/admin/byos/) Lite type workspaces.*

## What you can ask

- `List all active transfers for john@user.com`
- `List all files for job myupload`
- `Show the log for job myupload`
- `Pause job myupload`, `Resume job myupload` and `Abort transfer myupload`

## Set up in ChatGPT

You need [Node.js](https://nodejs.org) 18 or later, and an API key for your workspace. API keys are created the same way as for the Python API, see [How to create and manage API keys](/developer/python-api/#how-to-create-and-manage-api-keys).

1. In ChatGPT, open the settings and choose **Connect to a custom MCP**.
2. Enter the name `accsyn`.
3. Set the command to launch to the full path of `npx` (run `which npx` in a terminal to find it), and the argument to:

    ```bash
    -y accsyn-mcp-server
    ```

4. Add these environment variables:

    | Name | Value |
    | --- | --- |
    | `ACCSYN_WORKSPACE` | Your workspace code, for example `acmefilm`. |
    | `ACCSYN_API_USER` | The email of the API user, for example `john@user.com`. |
    | `ACCSYN_API_KEY` | The API key of that user. |

5. Save, restart ChatGPT, and start a new chat.
6. Ask: `List all active transfers for john@user.com`.

The agent acts as the API user, with the same permissions.

## More instructions

The setup for Claude Desktop and Claude Code, all tools and their arguments, and troubleshooting are in the [README on GitHub](https://github.com/accsyn/mcp-server/blob/main/README.md).
