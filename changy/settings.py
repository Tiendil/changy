import pydantic_settings


class BaseSettings(pydantic_settings.BaseSettings):
    model_config = pydantic_settings.SettingsConfigDict(
        env_nested_delimiter="__",
        # TODO: smart search for .env file
        # or update to pydantic-settings when it will be released
        env_file=("../.env", ".env"),
        extra="allow",
    )


class Settings(BaseSettings):
    changelog_name: str = "CHANGELOG.md"
    changelog_sources_dir: str = "changes"
    changelog_header: str = "header.md"

    changes_file_template: str = "changes_template.md"
    unreleased_changes_file: str = "unreleased.md"
    next_release_changes_file: str = "next_release.md"

    model_config = pydantic_settings.SettingsConfigDict(env_prefix="CHANGY_")


settings = Settings()
