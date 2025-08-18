title = soup.find("title")
    # if title:
    #     response["title"] = title.get_text()

    # # Extract the canonical URL
    # canonical_url = soup.find("link", rel="canonical")
    # if canonical_url:
    #     response["url"] = canonical_url["href"]

    # # Extract the description
    # description = soup.find("meta", attrs={"name": "description"})
    # if description:
    #     response["description"] = description["content"]

    # # Extract the date
    # date = soup.find("meta", attrs={"name": "date"})
    # if date:
    #     response["date"] = date["content"]

    # # Extract the author
    # author = soup.find("meta", attrs={"name": "author"})
    # if author:
    #     response["author"] = author["content"]

    # # Extract the links
    # for link in soup.find_all("a"):
    #     response["links"].append(link["href"])

    # # Extract the images
    # for img in soup.find_all("img"):
    #     response["images"].append(img["src"])

    # # Extract the videos
    # for video in soup.find_all("video"):
    #     response["videos"].append(video["src"])

    # # Extract the language
    # language = soup.find("html")
    # if language:
    #     response["language"] = language.get("lang", "")

    # # Extract the clean text
    # clean_text = soup.get_text()
    # response["clean_text"] = clean_text
    # response["word_count"] = len(clean_text.split())

    # # Extract the clean HTML
    # response["html"] = str(soup)

    # # Extract the assets (sections with headings and text)
    # headings = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
    # for heading in headings:
    #     section_text = heading.find_next(text=True, recursive=False)
    #     response["assets"].append({
    #         "heading": heading.text,
    #         "text": section_text
    #     })

    # # Extract the questions
    # questions = re.findall(r"[\w\s]+\?", clean_text)
    # response["questions"] = questions

    # # Extract the entities
    # entities = {}
    # for word in clean_text.split():
    #     if word in entities:
    #         entities[word] += 1
    #     else:
    #         entities[word] = 1
    # response["entities"] = sorted(entities.items(), key=lambda x: x[1], reverse=True)

    # # Extract the statistics
    # stats_pattern = r"\b\d+(\.\d+)?\b"
    # stats = re.findall(stats_pattern, clean_text)
    # response["statistics"] = stats