"""Main entry point for PostgreSQL MCP Server.

This module provides the CLI entry point for running the MCP server
using FastMCP with stdio transport.
"""

import asyncio
import sys

from pg_mcp.server import run_server


def main() -> None:
    """Main entry point for the PostgreSQL MCP Server.

    This function starts the FastMCP server using stdio transport,
    enabling communication with MCP clients.

    The server lifecycle is managed through the lifespan context manager,
    which handles:
    - Configuration loading
    - Database connection pool creation
    - Schema cache initialization
    - Service component setup
    - Graceful shutdown

    Example:
        Run the server:
        >>> python -m pg_mcp

        Run with environment variables:
        >>> DATABASE_HOST=localhost DATABASE_NAME=mydb python -m pg_mcp
    """
    try:
        asyncio.run(run_server())
    except KeyboardInterrupt:
        print("\nServer stopped by user")
        sys.exit(0)
    except Exception as e:
        print(f"Fatal error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
