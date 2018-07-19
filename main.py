from twisted.internet.task import react
import treq_test

if __name__ == "__main__":
    while True:
        try:
            print('Options:')
            print('1- Test with Treq')
            print('2- Test with Locust')
            print('4- Exit.')
            option = input("Enter your option: ")

            if int(option) == 1:
                print("Options:")
                print("1- Test Get multiple times")
                print("2- Test Post multiple times")
                print("3- Test Downloading files")
                treqoption = input("Enter your option: ")
                if int(treqoption) == 1:
                    url = input("Enter the url: ")
                    times = input("Enter the number of times to test: ")
                    if url != "":
                        react(treq_test.test_get_many, [url.strip(), int(times)])  # app url and times to test it
                elif int(treqoption) == 2:
                    url = input("Enter the url: ")
                    times = input("Enter the number of times to test: ")
                    if url != "":
                        react(treq_test.test_post_many, [url.strip(), int(times)])  # app url and times to test it
                elif int(treqoption) == 3:
                    url = input("Enter the url: ")
                    filename = input("Enter the name of the output file: ")
                    response = react(treq_test.download_file, [url.strip(), filename.strip()])
                else:
                    print("No option selected")

            elif int(option) == 2:
                print("to test with locust please run the following command from the terminal")
                print("locust --host=<BASE URL OF THE API>")
                print("and then go to localhost:8089 to run the tests")

            elif int(option) == 4:
                break

            else:
                print("No option selected")
        except Exception as e:
            print(e)
