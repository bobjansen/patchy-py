"""
Patches an existing function, creating a new one.
"""
import inspect
import diff_match_patch

def patch(original_fun):
    """
    Function decorator to apply the patch.
    """
    def wrapped(target):
        source = get_source(original_fun)
        diff = get_patch(target)
        new_source = apply_patch(source, diff)
        return create_fun(new_source)
    return wrapped


def apply_patch(source, diff):
    """
    Apply the patch in doc_string to source.
    """
    dmf = diff_match_patch.diff_match_patch()
    dmf_patch = dmf.patch_fromText(diff)
    new_source = dmf.patch_apply(dmf_patch, source)
    return new_source[0]


def get_patch(fun):
    """
    Get the patch that needs to be applied to this function.
    """
    return inspect.getdoc(fun)


def get_source(fun):
    """
    Get the source of function fun.
    """
    return inspect.getsource(fun)


def create_fun(source):
    """
    Create the function by execing patched source lines.

    The name of the function is retrieved by comparing locals before and after
    the exec. This could be extended so more than one function is created.
    """
    # Locals should start empty, later: closures.
    start_set = set(locals().keys())
    start_set.add('start_set')  # The set itself is also added to locals.
    exec(source)
    end_set = set(locals().keys())
    new_fun_name = end_set.difference(start_set).pop()
    return locals()[new_fun_name]

def create_patch(fun1, fun2):
    """
    Create a patch from fun1 to fun2.
    """
    dmf = diff_match_patch.diff_match_patch()
    source1 = inspect.getsource(fun1)
    source2 = inspect.getsource(fun2)

    diff = dmf.diff_lineMode(source1, source2, None)
    dmf_patch = dmf.patch_make(diff)
    return dmf.patch_toText(dmf_patch)

