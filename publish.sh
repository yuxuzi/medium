git add . && git commit -am"c profile" && git push 


git commit -a --amend --no-edit && git push


# Add changes to the staging area
git add .

# Commit changes
read -p "Enter commit message: " commit_message

git commit -m "$commit_message" && git push

curl -X POST -H "Content-Type: text/markdown" --data-binary @your_file.md http://example.com/endpoint
 
GET https://api.medium.com/v1/me

userid="1eddcbf38eca77702559bd1faa24bba988bc83f87bec96602ca3f6c3853a21e76"
url=https://api.medium.com/v1/users/$userid/posts

content=$(cat markdown/cprofile.md)
token="22d42ebe7f9f4202949d537ed20e7f4f3847af1fcc17f87009a27f4fb6301534d"
jq -n \
  --arg title "Test post via api" \
  --arg contentFormat "markdown" \
  --arg content "$content" \
  '{title: $title, contentFormat: $contentFormat, content: $content}' | \
curl --oauth2-bearer $token -H "Content-Type: application/json" --data-binary @- -X POST $url
