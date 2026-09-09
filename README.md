# Lily public legal documents

- [Privacy Policy](https://zina26.github.io/lily-legal/privacy.html) — `privacy-policy.md`; `privacy.html` and `index.html` carry the same policy.
- [Terms of Service](https://zina26.github.io/lily-legal/terms.html) — `terms-of-service.md` is the source; `terms.html` is generated.
- [Support](https://zina26.github.io/lily-legal/support.html) — `support.html` is hand-written (contact email, FAQ on subscription / data / voice); the URL is what goes in App Store Connect's required Support URL field.

## Editing and publishing terms

1. Edit `terms-of-service.md` first. Check factual promises against the current Privacy Policy and actual service behavior.
2. Run `python3 scripts/build_terms.py`. This dependency-free generator supports the document's headings, paragraphs, bold text, and links and reuses the privacy page's CSS. It fails on unsupported block syntax.
3. Verify all sections and links, compare the complete Markdown and rendered text, and check desktop/mobile readability. Independently review material legal or privacy changes.
4. Commit the document and generated page. Record the change and its commit in `PROGRESS.md`.
5. Publishing to `main` deploys through the repository's existing GitHub Pages root configuration. Verify deployment success and compare the public document with the committed artifact.

## App integration still to complete

Publishing this site does not change the iOS app or App Store Connect.

- Point the app's Lily service-terms link to `https://zina26.github.io/lily-legal/terms.html` and verify onboarding, settings, and purchase flows open it.
- Version and record acceptance of the Lily terms; do not treat acceptance of the prior Apple-only terms as acceptance of this document. Handle existing users and future material updates accordingly.
- Keep Apple's Standard EULA as the app license. These service terms supplement it; they are not a custom EULA to paste into App Store Connect's custom-license field. Retain the required Apple EULA reference where applicable and add the Lily service-terms link to the appropriate user-facing metadata.
- App integration must follow the Lily repository's frozen UI and release review requirements.

## Editorial references

The initial terms were prepared at the product owner's request using Rosebud's concise organization and the supplied Pillowtalk text's voice/AI topics as references. Wording is specific to Lily; competitor company details, age thresholds, billing offers, broad content licenses, and blanket exclusions were not adopted.

- [Rosebud Terms of Service](https://help.rosebud.app/about-us/terms-of-service)
- Pillowtalk Terms of Service, updated April 4, 2025 (text supplied by the product owner).
- [Apple Standard EULA](https://www.apple.com/legal/internet-services/itunes/dev/stdeula/)
- [Apple subscription cancellation](https://support.apple.com/en-us/118428)
- [Apple refund guidance](https://support.apple.com/en-us/118223)

Content review checks consistency and unsupported promises; it is not legal certification. The existing Privacy Policy's substantive legal bases and provider practices were not re-audited as part of adding these terms.
