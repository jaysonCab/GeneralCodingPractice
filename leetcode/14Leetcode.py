def flowers(srts):
    smallestWord = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    commonPrefix = ''
    listing = []
    returnPrefix = ''

    for item in srts:
        if len(item) < len(smallestWord):
            smallestWord = item

    for item in strs:
        for i in range(len(smallestWord)):
            if item[i] == smallestWord[i]:
                commonPrefix += item[i]
            else:
                listing.append(commonPrefix)
                commonPrefix = ''
                break

    smallestWordinListing = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'


    print(f'Listing is {listing}')
    for item in listing:
        if len(item) < len(smallestWordinListing):
            returnPrefix = item
    
    return returnPrefix

strs = ["reflower","flow","flight"]
print(f'the common prefix is {flowers(strs)}')