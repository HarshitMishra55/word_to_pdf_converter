import pytest
from io import BytesIO
from word_to_pdf_converter.convert import convert_to_pdf


def test_convert_to_pdf():
    with open("test.docx", "rb") as f:
        pdf_buffer = convert_to_pdf(f)
        assert pdf_buffer is not None
        assert isinstance(pdf_buffer, BytesIO)


# To run tests
# poetry run pytest
