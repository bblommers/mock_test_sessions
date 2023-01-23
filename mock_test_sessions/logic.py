def get_stackname_from_changeset(session, change_set_name):
    try:
        # this uses session instead of the client directly, which is what started failing
        cloudformation_client = session.client("cloudformation", region_name="eu-west-1")
        response = cloudformation_client.describe_change_set(ChangeSetName=change_set_name)

        return response["StackName"]
    except Exception as e:
        print(e)
        return ""
