import requests


BASE_URL = "http://127.0.0.1:8000"


def print_result(method, url, response):
    print(f"\n{'=' * 70}")
    print(f"{method} {url}")
    print(f"Status: {response.status_code}")

    try:
        print(response.json())
    except Exception:
        print(response.text)


def test_crud(
    name: str,
    endpoint: str,
    create_data: dict,
    update_data: dict,
):
    print(f"\n\n{'#' * 80}")
    print(f"# TEST: {name}")
    print(f"{'#' * 80}")

    # ==================================================
    # 1. CREATE
    # ==================================================

    url = f"{BASE_URL}{endpoint}"

    response = requests.post(
        url,
        json=create_data,
    )

    print_result("POST", url, response)

    response.raise_for_status()

    created = response.json()

    # récupérer ID
    entity_id = created.get("id")

    if entity_id is None:
        raise RuntimeError(
            f"{name}: impossible de récupérer 'id' après POST"
        )

    # ==================================================
    # 2. GET BY ID
    # ==================================================

    url = f"{BASE_URL}{endpoint}{entity_id}"

    response = requests.get(url)

    print_result("GET", url, response)

    response.raise_for_status()

    # ==================================================
    # 3. GET ALL
    # ==================================================

    url = f"{BASE_URL}{endpoint}"

    response = requests.get(url)

    print_result("GET", url, response)

    response.raise_for_status()

    # ==================================================
    # 4. PATCH
    # ==================================================

    url = f"{BASE_URL}{endpoint}{entity_id}"

    response = requests.patch(
        url,
        json=update_data,
    )

    print_result("PATCH", url, response)

    response.raise_for_status()

    # ==================================================
    # 5. DELETE
    # ==================================================

    response = requests.delete(url)

    print_result("DELETE", url, response)

    response.raise_for_status()

    print(f"\n✓ {name} TEST PASSED")


# ==========================================================
# CATEGORY
# ==========================================================

test_crud(
    name="Category",
    endpoint="/categories/",
    create_data={
        "label": "TEST_CATEGORY",
    },
    update_data={
        "label": "TEST_CATEGORY_UPDATED",
    },
)


# ==========================================================
# SKILL
# ==========================================================

test_crud(
    name="Skill",
    endpoint="/skills/",
    create_data={
        "skill": "TEST_SKILL",
        "category_id": None,
    },
    update_data={
        "skill": "TEST_SKILL_UPDATED",
        "category_id": None,
    },
)


# ==========================================================
# CONTACT
# ==========================================================

test_crud(
    name="Contact",
    endpoint="/contacts/",
    create_data={
        "label": "TEST_CONTACT",
        "icon": "test-icon",
        "link": "https://example.com",
    },
    update_data={
        "label": "TEST_CONTACT_UPDATED",
        "icon": "updated-icon",
        "link": "https://example.org",
    },
)


# ==========================================================
# DIPLOMA
# ==========================================================

test_crud(
    name="Diploma",
    endpoint="/diplomas/",
    create_data={
        "name": "TEST_DIPLOMA",
        "establishment": "TEST_ESTABLISHMENT",
        "start_date": "2025-01-01",
        "end_date": "2026-01-01",
    },
    update_data={
        "name": "TEST_DIPLOMA_UPDATED",
        "establishment": "TEST_ESTABLISHMENT_UPDATED",
        "start_date": "2025-01-01",
        "end_date": "2026-06-01",
    },
)


# ==========================================================
# DOMAIN
# ==========================================================

test_crud(
    name="Domain",
    endpoint="/domains/",
    create_data={
        "label": "TEST_DOMAIN",
    },
    update_data={
        "label": "TEST_DOMAIN_UPDATED",
    },
)


# ==========================================================
# FRAMEWORK
# ==========================================================

test_crud(
    name="Framework",
    endpoint="/frameworks/",
    create_data={
        "label": "TEST_FRAMEWORK",
    },
    update_data={
        "label": "TEST_FRAMEWORK_UPDATED",
    },
)


# ==========================================================
# KEYWORD
# ==========================================================

test_crud(
    name="Keyword",
    endpoint="/keywords/",
    create_data={
        "label": "TEST_KEYWORD",
    },
    update_data={
        "label": "TEST_KEYWORD_UPDATED",
    },
)


# ==========================================================
# LANGUAGE
# ==========================================================

test_crud(
    name="Language",
    endpoint="/languages/",
    create_data={
        "code": "xx",
        "label": "Test Language",
    },
    update_data={
        "code": "xy",
        "label": "Test Language Updated",
    },
)


# ==========================================================
# NAVIGATION
# ==========================================================

test_crud(
    name="Navigation",
    endpoint="/navigations/",
    create_data={
        "label": "TEST_NAVIGATION",
        "enabled": True,
        "position": 999,
    },
    update_data={
        "label": "TEST_NAVIGATION_UPDATED",
        "enabled": False,
        "position": 1000,
    },
)


# ==========================================================
# PROGRAMMING LANGUAGE
# ==========================================================

test_crud(
    name="ProgrammingLanguage",
    endpoint="/programming-languages/",
    create_data={
        "label": "TEST_PROGRAMMING_LANGUAGE",
    },
    update_data={
        "label": "TEST_PROGRAMMING_LANGUAGE_UPDATED",
    },
)


# ==========================================================
# SUBDOMAIN
# ==========================================================

test_crud(
    name="Subdomain",
    endpoint="/subdomains/",
    create_data={
        "label": "TEST_SUBDOMAIN",
    },
    update_data={
        "label": "TEST_SUBDOMAIN_UPDATED",
    },
)


# ==========================================================
# TAG
# ==========================================================

test_crud(
    name="Tag",
    endpoint="/tags/",
    create_data={
        "label": "TEST_TAG",
    },
    update_data={
        "label": "TEST_TAG_UPDATED",
    },
)