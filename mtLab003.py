import lab_chat as lc #importing previously written code and aliasing it (to make it easier to call functions from it)

#Parameter and Conditional
def get_user_input(message, to_upper=True):
    if to_upper:
        response = input(message).strip().upper()
    else:
        response = input(message).strip()
    return response

# get_username function creation
def get_username():
    return get_user_input("Enter your Username:").strip().upper()
# get_user function test
username = get_username()
#print(username)

# get_group function creation:
def get_group():
    return get_user_input("Enter your Group Name:").strip().upper()
# get_group function test:
group = get_group()
#print(group)

# get_message function creation
def get_message():
    return get_user_input("Enter your Message:", to_upper=False).strip()
# get_message function test:
message = get_message()
#print(message)

# initialize_chat function creation
def initialize_chat():
    user = username()
    group = get_group()
    node = lc.get_peer_node(user) # to connect as a peer node
    lc.join_group(node, group)
    channel = lc.get_channel(node, group)
    return channel
# initialize_chat function test

# start_chat function creation
def start_chat():
    channel = initialize_chat()

    while True:
        try: #tries to catch error
            msg = get_message()
            channel.send(msg.encode('utf_8'))
        except (KeyboardInterrupt, SystemExit):
            break #if error is caught, stop running
    channel.send("$$STOP".encode('utf_8'))
    print("FINISHED")

print(type(initialize_chat()))
start_chat()

