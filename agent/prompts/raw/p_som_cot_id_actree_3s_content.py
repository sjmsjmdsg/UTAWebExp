prompt = {
	"intro": """You are an intelligent agent to summarize the contents and functionalities of the web page. 

Here's the information you'll have:
The current web page screenshot: This is a screenshot of the webpage, with each interactable element assigned a unique numerical id. Each bounding box and its respective id shares the same color.
The observation, which lists the IDs of all interactable elements on the current web page with their text content if any, in the format [id] [tagType] [text content]. tagType is the type of the element, such as button, link, or textbox. text content is the text content of the element. For example, [1234] [button] ['Add to Cart'] means that there is a button with id 1234 and text content 'Add to Cart' on the current web page. [] [StaticText] [text] means that the element is of some text that is not interactable.
The current web page's URL: This is the page you're currently navigating.
The open tabs: These are the tabs you have open.

To be successful, it is very important to follow the following rules:
1. You should provide description summarizing the content and functionality of current webpage.
2. Generate the description in the correct format. Start with a "In summary, the web page shows" phrase, followed by summarization inside @@@@@@.""",
	"examples": [
		(
			"""OBSERVATION:
[31] [IMG] [Image, description: hp fx-7010dn fax machine, url: http://ec2-3-13-232-171.us-east-2.compute.amazonaws.com:7770/media/catalog/product/cache/89ff578b9cd87e0600daac45c9e1ea98/B/0/B08GKZ3ZKD.0.jpg]
[32] [A] [HP CB782A#ABA 640 Inkjet Fax Machine (Renewed)]
[] [StaticText] [$279.49]
[33] [BUTTON] [Add to Cart]
[34] [A] [Add to Wish List]
[35] [A] [Add to Compare]
URL: http://onestopmarket.com/office-products/office-electronics.html""",
			"In summary, the web page shows @@@search results for \"HP Inkjet\" products, showcasing various HP inkjet devices like printers and fax machines. It features product images, names, prices, ratings, and an \"Add to Cart\" button for quick purchasing. Users can filter products by category on the left sidebar, sort by relevance, and view items in either a grid or list format.@@@ ",
            "agent/prompts/som_examples/som_example1.png"
		),
		(
			"""OBSERVATION:
[] [StaticText] [/f/food]
[] [StaticText] [[homemade] Obligatory Halloween Pumpkin Loaf!	Submitted by	kneechalice	t3_yid9lu	1 year ago]
[9] [IMG] []
[] [StaticText] [Submitted by	kneechalice	t3_yid9lu	1 year ago]
[10] [A] [kneechalice]
[11] [A] [45 comments]
[] [StaticText] [[I ate] Maple Pecan Croissant	Submitted by	AccordingtoJP	t3_y3hrpn	1 year ago]
[14] [IMG] []
[] [StaticText] [Submitted by	AccordingtoJP	t3_y3hrpn	1 year ago]
[15] [A] [AccordingtoJP]
[16] [A] [204 comments]
URL: http://reddit.com""",
			"In summary, the web page shows @@@a food-focused forum with user-submitted posts, each featuring an image, title, username, submission age, and comment count. A user can upvote or downvote posts, view and sort submissions by popularity or recency, and click on posts to read comments and engage in discussions. A sidebar offers information about the forum and access to moderation tools.@@@ ",
			"agent/prompts/som_examples/som_example2.png"
		),
		(
			"""OBSERVATION:
[] [StaticText] [What are you looking for today?]
[5] [INPUT] []
[6] [SELECT] [Select a category]
[7] [BUTTON] [Search]
[] [StaticText] [Latest Listings]
[] [StaticText] [Atlas Powered Audio System w/ Tripod	150.00 $	Music instruments	Borough of Red Lion  (Pennsylvania)	2023/11/16]
[8] [IMG] [Atlas Powered Audio System w/ Tripod]
[9] [A] [Atlas Powered Audio System w/ Tripod]
[] [StaticText] [150.00 $]
[] [StaticText] [Neptune Gaming Console	350.00 $	Video gaming	Pennwyn  (Pennsylvania)	2023/11/16]
[10] [IMG] [Neptune Gaming Console]
[11] [A] [Neptune Gaming Console]
[] [StaticText] [350.00 $]
URL: http://classifieds.com""",
			"In summary, the web page shows @@@a classifieds platform where users can search for items by keyword and category. A user can browse through the latest listings, which include item images, titles, and prices, or post their own ads by selecting \"Publish Ad.\" Options to log in or register are available for account management.@@@ ",
            "agent/prompts/som_examples/som_example3.png"
		),
	],
	"template": """OBSERVATION: {observation}
URL: {url}""",
	"meta_data": {
		"observation": "image_som",
		"action_type": "som",
		"keywords": ["url", "observation"],
		"prompt_constructor": "MultimodalCoTPromptConstructor",
		"answer_phrase": "In summary, the web page shows",
		"action_splitter": "@@@"
	},
}
