# Aman Resume Portfolio

## Original problem statement
this is my resume and photo could you please make ready to deploy website for me ??

## Architecture decisions
- React single-page portfolio with responsive CSS and uploaded profile photo/resume assets.
- FastAPI endpoint stores private contact inquiries in MongoDB using the configured `MONGO_URL` and `DB_NAME`.
- Direct phone and email are intentionally not rendered publicly; visitors use the inquiry form.

## Implemented
- Corporate white portfolio homepage with hero, about, experience timeline, skills toolkit, selected projects, education and certifications.
- Functional navigation, mobile menu, LinkedIn/GitHub profile links, resume download link and private inquiry modal.
- Server-side inquiry validation and success/error feedback.

## Prioritized backlog
- P0: Confirm Aman’s exact LinkedIn and GitHub usernames if different from the current profile destinations.
- P1: Add an admin-only inbox or email notification for incoming inquiries.
- P2: Add a printable case-study page for the AWS three-tier and EKS projects.

## Next tasks
- Replace social destinations if Aman provides verified profile URLs.
- Add inquiry notification delivery when a messaging provider is selected.