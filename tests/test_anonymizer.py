from app.anonymizer import Anonymizer


def test_anonymize_and_rehydrate():
    text = "Policy 123456 belongs to John Doe."
    anonymizer = Anonymizer()
    anon, mapping = anonymizer.anonymize_text(text)
    assert anon != text
    rehydrated = anonymizer.rehydrate_text(anon, mapping)
    assert rehydrated == text
