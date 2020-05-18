import pytest
def pytest_collection_modifyitems(session, config, items:list):
    for item in items:
        print(item.nodeid)
        if 'add' in item.nodeid:
            item.add_marker(pytest.mark.add)
        if 'sub' in item.nodeid:
            item.add_marker(pytest.mark.sub)
        if 'div' in item.nodeid:
            item.add_marker(pytest.mark.div)
        if 'mul' in item.nodeid:
            item.add_marker(pytest.mark.mul)