from tensorflow.keras.applications import Xception
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Flatten, Dropout
from tensorflow.keras.models import Model

def add_model_head(base_model, n_categories):
    """
    Takes a base model and adds a pooling and a softmax output based on the number of categories

    Args:
        base_model (keras Sequential model): model to attach head to
        n_categories (int): number of classification categories

    Returns:
        keras Sequential model: model with new head
        """

    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    predictions = Dense(n_categories, activation='softmax')(x)
    model = Model(inputs=base_model.input, outputs=predictions)
    return model

def create_transfer_model(input_size, n_categories, weights = 'imagenet', model=Xception):
    """
    Creates model without top and attaches new head to it
    Args:
        input_size (tuple(int, int, int)): 3-dimensional size of input to model
        n_categories (int): number of classification categories
        weights (str or arg): weights to use for model
        model (keras Sequential model): model to use for transfer
    Returns:
        keras Sequential model: model with new head
        """
    base_model = model(weights=weights,
                      include_top=False,
                      input_shape=input_size)
    model = add_model_head(base_model, n_categories)
    return model
