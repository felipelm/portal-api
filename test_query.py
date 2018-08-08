from gql import gql, Client
from schema import schema

query_str = """{
  allDepartments {
    pageInfo {
      hasNextPage
      hasPreviousPage
      startCursor
      endCursor
    }
    edges {
      node {
        id
        name
        employees {
          edges {
            node {
              name
              id
            }
          }
        }
      }
    }
  }
}"""

from gql import gql, Client
client = Client(schema=schema)
query = gql(query_str)

print(client.execute(query))