from main import(
firstfunc,
onefunc,
countvowels,
removeduplicates

)

def test_firstfunc():
    assert firstfunc("hi") == "hi"
def test_onefunc():
    assert onefunc("HELLO") == "olleh"
def test_countvowels():
    assert countvowels("борщ") == 1 
def test_remove_duplicates():
    assert removeduplicates("анна") == "ан"