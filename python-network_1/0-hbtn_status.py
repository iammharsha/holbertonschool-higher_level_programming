#!/usr/bin/python3
"""Module to get status"""
import urllib.request


if __name__ == "__main__":
    """Module to call api https://intranet.hbtn.io/status"""
    url = 'https://intranet.hbtn.io/status'
    headers = {
        'cookie': '_ga=GA1.2.1776982423.1712752155; context_user_curriculum_status_id=eyJfcmFpbHMiOnsibWVzc2FnZSI6Ik16QTNNVEE9IiwiZXhwIjpudWxsLCJwdXIiOiJjb29raWUuY29udGV4dF91c2VyX2N1cnJpY3VsdW1fc3RhdHVzX2lkIn19--63e90e5d517f49b9eecd59a3f27e7567861abcf1; context_curriculum_id=eyJfcmFpbHMiOnsibWVzc2FnZSI6Ik1qazEiLCJleHAiOm51bGwsInB1ciI6ImNvb2tpZS5jb250ZXh0X2N1cnJpY3VsdW1faWQifX0%3D--cbb9fb9823fc13cb7c544a7ee1db56b8b315e066; timezone=8; _gid=GA1.2.575380488.1720243111; cf_clearance=IqlsmGlcSeMP5bfSbeaYY2KBlVvjJ1t.B5qa0KDpY9E-1720254320-1.0.1.1-rc9MvhAeRQWzS7zEa6JhRSBLsZ2lhg.wkKc28yFblISz7DFmJLhMWK_9C4U0vSkNNQyym0mRCCkC6fb.JOAVDw; _ga_E61MDMQF4S=GS1.2.1720254324.35.1.1720255569.28.0.0; _holberton_intranet_session=EnDoYx%2F%2B4c9GVVNlU7HUN9mwlTZfau65oLQzVWY4cpjqFPFwu3v%2B6HJevz2zxO0QS0eN06ESzT73h61hvifNLahn8puwyop2T4m1TWhvUvrFAZpa3tv4ZF6EZOUs78Vjg9RsN6ce4p16JD9q1R7EgKch17mDfy9wCd4yR7dKnWAwovST1U5IEDurQVIoQ2%2BySenIU54xQ7ud%2BSm8NgkLuRl1EQEXvlGt4h9qTi0uH3eaZvzI%2BnzdrxTbStUrtvyAuqeCLqNQydzaPTAbJBVYnJduKA8mYRQR81LfhkYS3gda0zF%2F5CwwQQL8OALQTwfCF%2B7xsASoeYH%2FcctjGYOuRlnMtSXLRmLuv5XJNEzdl0QWZcwVEh1MjzXvvK%2BpGBTn9m5lp6LX6RdC918mTKt4bACh09rjkb8Vpjrf0dsdWJax8naQxqjsyxGYvotJH5Oco0hzQo800ZB1g3sQ7mwtX97MdXURv0xC46Y6dl%2FfhwVmv6hIALSg2ak7yA%3D%3D--SvDQIOPpxtBbkef%2B--35cZ8vyzaRzQ70%2BljSaLbw%3D%3D; _holberton_intranet_session=fVWBHcztr3RNYazAh43pz4Ay45%2FWGTVU1bfwHwEgSEEmOd1IuMEloNC80GJ1ti4JYVYNAfpcPI2W3ugp91a%2BcqcirZJKmoCy7qYDJAUnFs5VBSbJX91O0VHki2TJMJ6FCslGdEWsdBMQr9or7wG%2BgmOglJKXJZHy3nUADOBb4ecVaEnStvWXEMG7hu5fgWnarc0o2jFNLU9XvZo0YbmuWyOlBEPBWI0RRwMsD7g12pES9d5WmCm1VUNvWvYSZkPfvrbXOuOVhHgHxztpdZZygMP0pP9C7iqCbeqLa5Xo51fHnQdqm9SsP2Jr6q6e8M5xw6MBV3PZD7ovg6DTCfgVjLE9EldfIV1S1SUoB%2BUh%2Fusi5eHOgmUmaUCgC5ztVyYGRzrXLJvb3F00%2BXy2IeIauW8xBK6Qu1PM3%2F1jctik8zZcip%2FMmCubvoxJmyDQ1Qhp5MDFQvz3cgsw5MYe66fWkZSrGD4CXGi8bDBq585Yj3loQfljWmDlzIoYrA%3D%3D--TbVDmGN7YUU4xcAD--M3U%2FjJAPaZWwE3KIBJXWMg%3D%3D; context_curriculum_id=eyJfcmFpbHMiOnsibWVzc2FnZSI6Ik1qazEiLCJleHAiOm51bGwsInB1ciI6ImNvb2tpZS5jb250ZXh0X2N1cnJpY3VsdW1faWQifX0%3D--cbb9fb9823fc13cb7c544a7ee1db56b8b315e066; context_user_curriculum_status_id=eyJfcmFpbHMiOnsibWVzc2FnZSI6Ik16QTNNVEE9IiwiZXhwIjpudWxsLCJwdXIiOiJjb29raWUuY29udGV4dF91c2VyX2N1cnJpY3VsdW1fc3RhdHVzX2lkIn19--63e90e5d517f49b9eecd59a3f27e7567861abcf1; timezone=8',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    request = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(request) as response:
        content = response.read()
        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
        print("\t- utf8 content:", content.decode('utf-8'))
