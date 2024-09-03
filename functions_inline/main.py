def main(params):
  print("helen-testing-function-123")
  name = params.get("name", "world")
  greeting = "Hello " + name + "!"

  return {
        "headers": {
            "Content-Type": "application/json",
        },
        "statusCode": 200,
        "body": greeting,
  }
