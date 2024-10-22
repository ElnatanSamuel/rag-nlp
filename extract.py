documents = [
    {
        "id": "doc1",
        "text": "Shipping Policy: Our standard shipping policy ensures that all orders are processed within 2-3 business days. \
        Domestic shipping typically takes 5-7 business days, while international shipping can take between 10-14 business days. \
        Customers will receive a tracking number once the order has been shipped. During peak seasons or promotions, processing and shipping times may be delayed. \
        For express shipping, we offer 2-day and overnight options at an additional cost. Shipping charges depend on the weight and destination of the order."
    },
    {
        "id": "doc2",
        "text": "Return and Exchange Policy: Customers may return items within 30 days of receipt for a full refund. \
        To be eligible for a return, the product must be unused, in its original packaging, and accompanied by a receipt or proof of purchase. \
        Some items such as perishable goods, custom products, and personal care items are not eligible for returns. \
        Exchanges are processed for defective or damaged items within 15 days of delivery. Refunds will be processed within 5-7 business days after receiving the returned item."
    },
    {
        "id": "doc3",
        "text": "Warranty Policy: Most of our electronics products come with a 1-year manufacturer's warranty that covers manufacturing defects. \
        If the product becomes defective during the warranty period, we will repair or replace it at no additional cost. \
        The warranty does not cover damage caused by improper use, unauthorized repairs, or accidental damage. \
        To claim a warranty, customers should contact our support team with proof of purchase and a description of the issue."
    },
    {
        "id": "doc4",
        "text": "Order Cancellation Policy: Orders can be canceled within 24 hours of placement for a full refund. \
        Once the order has been processed or shipped, cancellations are no longer possible. However, customers can still initiate a return or exchange after receiving the product. \
        Orders placed during promotional events may be subject to additional restrictions."
    },
    {
        "id": "doc5",
        "text": "Loyalty Program: Our loyalty program rewards customers with points for each purchase. \
        For every dollar spent, customers earn 10 points. Accumulated points can be redeemed for discounts on future purchases. \
        Members of the loyalty program also receive early access to sales, special promotions, and free shipping on all orders. \
        Points expire after 12 months of inactivity in the loyalty program. Customers can track their points through their account dashboard."
    },
    {
        "id": "doc6",
        "text": "Payment Issues: If a payment fails to go through, customers should first verify that their card details are correct and that they have sufficient funds. \
        We accept all major credit cards, PayPal, and Apple Pay. If the issue persists, we recommend reaching out to your card issuer or using a different payment method. \
        Payments made through PayPal may take up to 24 hours to be verified. Any orders not paid for within 48 hours will be automatically canceled."
    },
    {
        "id": "doc7",
        "text": "Promotions and Discounts: We offer seasonal promotions, including discounts, free shipping, and buy-one-get-one-free deals. \
        Customers should ensure that they enter the correct promo code at checkout to avail the offer. Promo codes cannot be combined with other discounts unless otherwise stated. \
        Some items, such as electronics and clearance items, may be excluded from promotions. All promotions have an expiration date, and offers are subject to availability."
    },
    {
        "id": "doc8",
        "text": "Product Reviews and Ratings: Customers are encouraged to leave product reviews after making a purchase. \
        Reviews help other shoppers make informed decisions. Customers can rate products on a scale of 1 to 5 stars, and leave comments regarding the quality, performance, and value of the product. \
        We reserve the right to remove any reviews that are offensive or violate our terms of service. Verified buyers' reviews are marked with a 'Verified Purchase' badge."
    },
    {
        "id": "doc9",
        "text": "Account Management: Customers can create and manage their accounts on our platform. \
        Through their accounts, they can view order history, track shipments, save their favorite items, and update their contact and payment information. \
        For security reasons, customers are advised to change their passwords regularly and use two-factor authentication. \
        If a customer forgets their password, they can use the 'Forgot Password' link to reset it via email."
    },
    {
        "id": "doc10",
        "text": "Gift Cards: We offer gift cards that can be purchased in denominations ranging from $10 to $500. \
        Gift cards can be used to purchase any item on our platform and never expire. They can be sent via email or printed and mailed to the recipient. \
        To redeem a gift card, customers must enter the gift card code during checkout. Gift cards cannot be reloaded or exchanged for cash."
    }
]

def get_document_text(doc_id):
    doc_lookup = {
        'doc1_chunk_0' :  "Shipping Policy: Our standard shipping policy ensures that all orders are processed within 2-3 business days.         Domestic shipping typically takes 5-7 business days, while international shipping "  ,

'doc1_chunk_1' :  "s 5-7 business days, while international shipping can take between 10-14 business days.         Customers will receive a tracking number once the order has been shipped. During peak seasons or promoti"  ,

'doc1_chunk_2' :  "r has been shipped. During peak seasons or promotions, processing and shipping times may be delayed.         For express shipping, we offer 2-day and overnight options at an additional cost. Shipping "  ,

'doc1_chunk_3' :  "overnight options at an additional cost. Shipping charges depend on the weight and destination of the order."  ,

'doc2_chunk_0' :  "Return and Exchange Policy: Customers may return items within 30 days of receipt for a full refund.         To be eligible for a return, the product must be unused, in its original packaging, and acco"  ,

'doc2_chunk_1' :  "ust be unused, in its original packaging, and accompanied by a receipt or proof of purchase.         Some items such as perishable goods, custom products, and personal care items are not eligible for "  ,

'doc2_chunk_2' :  "cts, and personal care items are not eligible for returns.         Exchanges are processed for defective or damaged items within 15 days of delivery. Refunds will be processed within 5-7 business days"  ,

'doc2_chunk_3' :  "Refunds will be processed within 5-7 business days after receiving the returned item."  ,

'doc3_chunk_0' :  "Warranty Policy: Most of our electronics products come with a 1-year manufacturer's warranty that covers manufacturing defects.         If the product becomes defective during the warranty period, we "  ,

'doc3_chunk_1' :  " becomes defective during the warranty period, we will repair or replace it at no additional cost.         The warranty does not cover damage caused by improper use, unauthorized repairs, or accidenta"  ,

'doc3_chunk_2' :  "y improper use, unauthorized repairs, or accidental damage.         To claim a warranty, customers should contact our support team with proof of purchase and a description of the issue."  ,

'doc3_chunk_3' :  "ase and a description of the issue."  ,

'doc4_chunk_0' :  "Order Cancellation Policy: Orders can be canceled within 24 hours of placement for a full refund.         Once the order has been processed or shipped, cancellations are no longer possible. However, c"  ,

'doc4_chunk_1' :  ", cancellations are no longer possible. However, customers can still initiate a return or exchange after receiving the product.         Orders placed during promotional events may be subject to additi"  ,

'doc4_chunk_2' :  "during promotional events may be subject to additional restrictions."  ,

'doc5_chunk_0' :  "Loyalty Program: Our loyalty program rewards customers with points for each purchase.         For every dollar spent, customers earn 10 points. Accumulated points can be redeemed for discounts on futu"  ,

'doc5_chunk_1' :  "lated points can be redeemed for discounts on future purchases.         Members of the loyalty program also receive early access to sales, special promotions, and free shipping on all orders.         "  ,

'doc5_chunk_2' :  "motions, and free shipping on all orders.         Points expire after 12 months of inactivity in the loyalty program. Customers can track their points through their account dashboard."  ,

'doc5_chunk_3' :  " through their account dashboard."  ,

'doc6_chunk_0' :  "Payment Issues: If a payment fails to go through, customers should first verify that their card details are correct and that they have sufficient funds.         We accept all major credit cards, PayPa"  ,

'doc6_chunk_1' :  "s.         We accept all major credit cards, PayPal, and Apple Pay. If the issue persists, we recommend reaching out to your card issuer or using a different payment method.         Payments made thro"  ,

'doc6_chunk_2' :  "fferent payment method.         Payments made through PayPal may take up to 24 hours to be verified. Any orders not paid for within 48 hours will be automatically canceled."  ,

'doc6_chunk_3' :  "utomatically canceled."  ,

'doc7_chunk_0' :  "Promotions and Discounts: We offer seasonal promotions, including discounts, free shipping, and buy-one-get-one-free deals.         Customers should ensure that they enter the correct promo code at ch"  ,

'doc7_chunk_1' :  "nsure that they enter the correct promo code at checkout to avail the offer. Promo codes cannot be combined with other discounts unless otherwise stated.         Some items, such as electronics and cl"  ,

'doc7_chunk_2' :  "ed.         Some items, such as electronics and clearance items, may be excluded from promotions. All promotions have an expiration date, and offers are subject to availability."  ,

'doc7_chunk_3' :  "re subject to availability."  ,

'doc8_chunk_0' :  "Product Reviews and Ratings: Customers are encouraged to leave product reviews after making a purchase.         Reviews help other shoppers make informed decisions. Customers can rate products on a sc"  ,

'doc8_chunk_1' :  "med decisions. Customers can rate products on a scale of 1 to 5 stars, and leave comments regarding the quality, performance, and value of the product.         We reserve the right to remove any revie"  ,

'doc8_chunk_2' :  ".         We reserve the right to remove any reviews that are offensive or violate our terms of service. Verified buyers' reviews are marked with a 'Verified Purchase' badge."  ,

'doc8_chunk_3' :  "erified Purchase' badge."  ,

'doc9_chunk_0' :  "Account Management: Customers can create and manage their accounts on our platform.         Through their accounts, they can view order history, track shipments, save their favorite items, and update "  ,

'doc9_chunk_1' :  " shipments, save their favorite items, and update their contact and payment information.         For security reasons, customers are advised to change their passwords regularly and use two-factor auth"  ,

'doc9_chunk_2' :  " their passwords regularly and use two-factor authentication.         If a customer forgets their password, they can use the 'Forgot Password' link to reset it via email."  ,

'doc9_chunk_3' :  " reset it via email."  ,

'doc10_chunk_0' :  "Gift Cards: We offer gift cards that can be purchased in denominations ranging from $10 to $500.         Gift cards can be used to purchase any item on our platform and never expire. They can be sent "  ,

'doc10_chunk_1' :  "n our platform and never expire. They can be sent via email or printed and mailed to the recipient.         To redeem a gift card, customers must enter the gift card code during checkout. Gift cards c"  ,

'doc10_chunk_2' :  "r the gift card code during checkout. Gift cards cannot be reloaded or exchanged for cash."  ,

    }
    return doc_lookup.get(doc_id, "")

def chunk_text(text, max_length=200, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = min(len(text), start + max_length)
        chunk = text[start:end]
        chunks.append(chunk)
        start += max_length - overlap
    return chunks

chunked_documents = []
for doc in documents:
    chunks = chunk_text(doc['text'])
    for i, chunk in enumerate(chunks):
        chunked_documents.append({
            "id": f"{doc['id']}_chunk_{i}",
            "text": chunk
        })

# for chunk in chunked_documents:
#     print(f"'{chunk['id']}'", ":", f""" "{chunk['text']}" ""","," ,"\n")
    
    
import os
from pinecone import Pinecone, ServerlessSpec
from sentence_transformers import SentenceTransformer

pc = Pinecone(
        api_key="ef9acd93-1774-49ad-8417-81d8841e0894"
    )

index_name = "ecommerce-support"
if index_name not in pc.list_indexes().names():
        pc.create_index(
            name="ecommerce-support",
            dimension=384,
            metric='euclidean',
            spec=ServerlessSpec(
                cloud='aws',
                region='us-east-1'
            )
        )

index = pc.Index(index_name)

embedder = SentenceTransformer('all-MiniLM-L6-v2')

for chunk in chunked_documents:
    embedding = embedder.encode(chunk['text']).tolist()
    index.upsert([(chunk['id'], embedding)])
    
    
def retrieve_documents(query):
    query_embedding = embedder.encode(query).tolist()

    result = index.query(vector=[query_embedding], top_k=1)
    print(result)
    return [match['id'] for match in result['matches']]

retrieve_documents("what is an your return policy")


from together import Together
def generate_response(prompt):
    client = Together(api_key="ee472495ec6514e25553987a73ed1f43fdfdd77938b4fed33aba5ebc5d7c45bc")
    stream = client.chat.completions.create(
            model="mistralai/Mixtral-8x7B-Instruct-v0.1",
            messages=[{"role": "user", "content": prompt}],
            stream=True,
    )
    print(stream)
    # result = []
    for chunk in stream:
        print(chunk.choices[0].delta.content or "", end="", flush=True)
        # result = chunk.choices[0].delta.content
        # print(result)
    return chunk.choices[0].delta.content

generate_response("what is the capital of ethiopia?")


# def create_customer_support_response(customer_query):
#     retrieved_docs = retrieve_documents(customer_query)

#     combined_docs = "\n".join([get_document_text(doc_id) for doc_id in retrieved_docs])
#     print(combined_docs)

#     final_prompt = f"Customer question: {customer_query}\n\nRelevant information:\n{combined_docs}"
#     return generate_response(final_prompt)
# create_customer_support_response("what is an your warranty like, eplain in 5 steps")



import spacy

nlp = spacy.load("en_core_web_sm")

def extract_keywords_and_intent(query):
    doc = nlp(query)
    keywords = [token.text for token in doc if not token.is_stop and not token.is_punct]
    # Simple intent recognition based on keywords
    if "difference" in keywords:
        intent = "comparison"
    else:
        intent = "general"
    print(keywords, intent)
    return keywords, intent


def create_customer_support_response(customer_query):
    keywords, intent = extract_keywords_and_intent(customer_query)
    
    retrieved_docs = retrieve_documents(customer_query)
    
    combined_docs = "\n".join([get_document_text(doc_id) for doc_id in retrieved_docs])
    
    if intent == "comparison":
        final_prompt = (
            f"Customer question: {customer_query}\n\n"
            f"Relevant information:\n{combined_docs}\n\n"
            "Please provide a clear comparison in 5 steps, highlighting the key differences."
        )
    elif intent == "steps":
        final_prompt = (
            f"Customer question: {customer_query}\n\n"
            f"Relevant information:\n{combined_docs}\n\n"
            "Please provide a step-by-step explanation."
        )
    else:
        final_prompt = (
            f"Customer question: {customer_query}\n\n"
            f"Relevant information:\n{combined_docs}\n\n"
            "Please provide a detailed response."
        )
    
    return generate_response(final_prompt)

create_customer_support_response("what is an your warranty like, explain in 5 steps")
