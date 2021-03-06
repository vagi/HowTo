# Get the tokenizer corresponding to our multilingual BERT model. 
# See TensorFlow Hub for more information about the model.

def get_tokenizer(bert_path=BERT_PATH_SAVEDMODEL):
    """Get the tokenizer for a BERT layer."""
    bert_layer = tf.saved_model.load(bert_path)
    bert_layer = hub.KerasLayer(bert_layer, trainable=False)
    vocab_file = bert_layer.resolved_object.vocab_file.asset_path.numpy()
    cased = bert_layer.resolved_object.do_lower_case.numpy()
    tf.gfile = tf.io.gfile  # for bert.tokenization.load_vocab in tokenizer
    tokenizer = bert.tokenization.FullTokenizer(vocab_file, cased)
  
    return tokenizer

tokenizer = get_tokenizer()

example_sentence = wiki_toxic_comment_train.iloc[37].comment_text[:150]
print(example_sentence)

example_tokens = tokenizer.tokenize(example_sentence)
print(example_tokens[:17])

example_input_ids = tokenizer.convert_tokens_to_ids(example_tokens)
print(example_input_ids[:17])
