class LossDataPackDict:
    """
    a wrapper for losses.

    return a dict of losses. The losses are values within a step.

    update each loss and sum them up to a total loss.
    call self.loss_dict to return the whole loss dict.

    ----------------------------------------------------
    Pseduo code to explain:
    loss = 0
    
    loss_1 = ...
    loss += loss_1
    
    loss_2 = ...
    loss += loss_2

    loss_dict = dict(
        loss_1 = loss_1,
        loss_2 = loss_2,
        loss = loss,
    )
    """
    def __init__(self,):
        self.losses = DataPackDict(loss=0)
    # def update(self,loss_dict):
        # self.losses.update(loss_dict)
        # self.losses.loss += list(loss_dict.values())[0]
    def update(self,**loss):
        self.losses.update(loss)
        # self.losses.loss += list(loss.values())[0]
        self.losses.loss += sum(loss.values())
    @property
    def loss_dict(self):
        return self.losses