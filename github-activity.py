import argparse
import requests

parser = argparse.ArgumentParser()

parser.add_argument("username", help="Type github username to show user activity. Example: python github-activity.py ArturChicharo", type=str)

args = parser.parse_args()

if args.username:
    url = f"https://api.github.com/users/{args.username}/events"

    response = requests.get(url)

    if response.status_code == 200:
        for event in response.json():
            if event['type'] == 'CommitCommentEvent':
                print(f"- User {event['actor']['login']} commented on a commit in {event['repo']['name']}")
            elif event['type'] == 'CreateEvent':
                print(f"- User {event['actor']['login']} created {event['payload']['ref_type']} {event['payload']['ref']} in {event['repo']['name']}")
            elif event['type'] == 'DeleteEvent':
                print(f"- User {event['actor']['login']} deleted {event['payload']['ref_type']} {event['payload']['ref']} in {event['repo']['name']}")
            elif event['type'] == 'ForkedEvent':
                print(f"- User {event['actor']['login']} forked {event['payload']['forkee']['full_name']}")
            elif event['type'] == 'GollumEvent':
                for page in event['payload']['pages']:
                    print(f"- User {event['actor']['login']} {event['payload']['action']} wiki page {page['page_name']} in {event['repo']['name']}")
            elif event['type'] == 'IssueCommentEvent':
                print(f"- User {event['actor']['login']} {event['payload']['action']} a comment on issue {event['payload']['issue']['number']} in {event['repo']['name']}")
            elif event['type'] == 'IssuesEvent':
                print(f"- User {event['actor']['login']} {event['payload']['action']} issue {event['payload']['issue']['number']} in {event['repo']['name']}")
            elif event['type'] == 'MemberEvent':
                print(f"- User {event['actor']['login']} {event['payload']['action']} user {event['payload']['member']['login']} in {event['repo']['name']}")
            elif event['type'] == 'PublicEvent':
                print(f"- User {event['actor']['login']} turned {event['repo']['name']} public")
            elif event['type'] == 'PullRequestEvent':
                if event['payload']['action'] == "synchronize":
                    print(f"- User {event['actor']['login']} synchronized pull request {event['payload']['pull_request']['id']} in {event['repo']['name']}")
                else:
                    print(f"- User {event['actor']['login']} {event['payload']['action']} pull request {event['payload']['pull_request']['id']} in {event['repo']['name']}")
            elif event['type'] == 'PullRequestReviewEvent':
                print(f"- User {event['actor']['login']} {event['payload']['action']} review {event['payload']['review']['id']} for pull request {event['payload']['pull_request']['id']} in {event['repo']['name']}")
            elif event['type'] == 'PullRequestReviewCommentEvent':
                print(f"- User {event['actor']['login']} {event['payload']['action']} comment {event['payload']['comment']['id']} for pull request review {event['payload']['pull_request']['id']} in {event['repo']['name']}")
            elif event['type'] == 'PullRequestReviewThreadEvent':
                print(f"- User {event['actor']['login']} marked comment thread {event['payload']['review_thread']['id']} as {event['payload']['action']} in {event['repo']['name']}")
            elif event['type'] == 'PushEvent':
                print(f"- User {event['actor']['login']} pushed {event['payload']['size']} commits to {event['repo']['name']}")
            elif event['type'] == 'ReleaseEvent':
                print(f"- User {event['actor']['login']} published release {event['payload']['release']['id']} to {event['repo']['name']}")
            elif event['type'] == 'SponsorshipEvent':
                print(f"- User {event['actor']['login']} {event['payload']['action']} sponsorship {event['payload']['sponsorship']['id']} in {event['repo']['name']}")
            elif event['type'] == 'WatchEvent':
                print(f"- User {event['actor']['login']} starred {event['repo']['name']}")
    else:
        print(f"Error fetching events: {response.status_code}")