--- ---

<h2>Commands</h2>

```
{createPost(...)}             ---> Create mutation

{post(id: "1"){id, ...}        ---> Read Query

{updatePOST(...)}              ---> Update Mutation

{deletePost(...)}              ---> Delete Mutation
```

Get Whole schema query
```GraphQL
    query IntrospectionQuery {
      __schema {
        
        queryType { name }
        mutationType { name }
        subscriptionType { name }
        types {
          ...FullType
        }
        directives {
          name
          description
          
          locations
          args {
            ...InputValue
          }
        }
      }
    }

    fragment FullType on __Type {
      kind
      name
      description
      
      fields(includeDeprecated: true) {
        name
        description
        args {
          ...InputValue
        }
        type {
          ...TypeRef
        }
        isDeprecated
        deprecationReason
      }
      inputFields {
        ...InputValue
      }
      interfaces {
        ...TypeRef
      }
      enumValues(includeDeprecated: true) {
        name
        description
        isDeprecated
        deprecationReason
      }
      possibleTypes {
        ...TypeRef
      }
    }

    fragment InputValue on __InputValue {
      name
      description
      type { ...TypeRef }
      defaultValue
      
      
    }

    fragment TypeRef on __Type {
      kind
      name
      ofType {
        kind
        name
        ofType {
          kind
          name
          ofType {
            kind
            name
            ofType {
              kind
              name
              ofType {
                kind
                name
                ofType {
                  kind
                  name
                  ofType {
                    kind
                    name
                  }
                }
              }
            }
          }
        }
      }
    }
  
```

- Paste the output in https://ivangoncharov.github.io/graphql-voyager/ (Visualiser)

---

<h2>More information</h2>

GraphQL can be more difficult to spot
* Usually you have some endpoint like gql?q=.. or graphql?q=... or g?q=...
+ An easier way to spot these is to try to find a reference to query or mutation
GraphQL has a major advantage for hackers though...
* It’s super easy to enumerate!

These also return JSON but it looks weird when compared to REST

However you probably need some practice forming queries
* Hacker101 GraphQL CTF levels! ---> 