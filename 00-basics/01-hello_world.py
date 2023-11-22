from prefect import flow

@flow(log_prints=True)
def hello_world(name: str = "World", goodbye: bool = False):
    print("Hello {name} from Prefect!")

    if goodbye:
        print("Goodbye {name} from Prefect!")

if __name__ == "__main__":
    hello_world.serve(name="my-first_deployment", tags=["onboarding"], parameters={"goodbye": True}, interval="60")
