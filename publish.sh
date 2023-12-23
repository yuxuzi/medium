git add. && git commit -am"f string' && git push 

# Add changes to the staging area
git add .

# Commit changes
read -p "Enter commit message: " commit_message

git commit -m "$commit_message" && git push

curl -X POST -H "Content-Type: text/markdown" --data-binary @your_file.md http://example.com/endpoint
 


userid="1eddcbf38eca77702559bd1faa24bba988bc83f87bec96602ca3f6c3853a21e76"
url=https://api.medium.com/v1/users/$userid/posts

content=$(cat markdown/match_case.md)

jq -n \
  --arg title "Test post via api" \
  --arg contentFormat "markdown" \
  --arg content "$content" \
  '{title: $title, contentFormat: $contentFormat, content: $content}' | \
curl --oauth2-bearer $token -H "Content-Type: application/json" --data-binary @- -X POST $url
