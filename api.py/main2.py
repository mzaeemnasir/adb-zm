import wordpressAPI


instance = wordpressAPI.Wordpress(
    "https://cryptomarketguides.com/xmlrpc.php", "crypto", "fuckedbyluna@69"
)

response = instance.new_post(
    title="Test Post", content="This is a test post from python"
)

print(response)
