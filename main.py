from fastmcp import FastMCP
from query import create_user,get_user_by_name


server = FastMCP("PostGreServer",instructions="This server provides access to a PostgreSQL database.")

@server.tool
def create_expense_user(name):
    """
    Create a new user in the PostgreSQL database.

    Use this tool when the user explicitly asks to create, register,
    or add a new user. The tool accepts the user's full name, creates
    a user ID based on the first and last name initials plus a
    four-digit sequence, stores the user in PostgreSQL, and returns
    the generated user ID.

    Args:
        name: The full name of the user. Expected format is
            "FirstName LastName".

    Returns:
        The generated user ID, for example "SG0001".
    """
    id = create_user(name)
    return id

@server.tool
def get_userid_from_username(name):
    """
    Retrieves the user ID associated with a given username.

    This function acts as an exposed server tool that wraps the database 
    lookup function to fetch a user's unique identifier.

    Args:
        name (str): The username to look up.

    Returns:
        str: The unique user ID corresponding to the username.
    """
    id = get_user_by_name(name)
    return id



if __name__ == "__main__":
    server.run(transport="http", port=7000)



