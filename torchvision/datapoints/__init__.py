import torch
from torchvision import _BETA_TRANSFORMS_WARNING, _WARN_ABOUT_BETA_TRANSFORMS

from ._bounding_box import BoundingBoxes, BoundingBoxFormat
from ._datapoint import Datapoint
from ._image import Image
from ._mask import Mask
from ._torch_function_helpers import set_return_type
from ._video import Video

if _WARN_ABOUT_BETA_TRANSFORMS:
    import warnings

    warnings.warn(_BETA_TRANSFORMS_WARNING)


def wrap(wrappee, *, like, **kwargs):
    """Convert a :class:`torch.Tensor` (``wrappee``) into the same :class:`~torchvision.datapoint.Datapoint` subclass as ``like``.

    If ``like`` is a :class:`~torchvision.datapoint.BoundingBoxes`, the ``format`` and ``canvas_size`` of
    ``like`` are assigned to ``wrappee``, unless they are passed as ``kwargs``.

    Args:
        wrappee (Tensor): The tensor to convert.
        like (Datapoint): The
        kwargs: Can contain "format" and "canvas_size" if ``like`` is a :class:`~torchvision.datapoint.BoundingBoxes`.
            Ignored otherwise.
    """
    if isinstance(like, BoundingBoxes):
        return BoundingBoxes._wrap(
            wrappee,
            format=kwargs.get("format", like.format),
            canvas_size=kwargs.get("canvas_size", like.canvas_size),
        )
    else:
        return wrappee.as_subclass(type(like))
