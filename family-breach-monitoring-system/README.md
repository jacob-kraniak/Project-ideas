# Family Breach Monitoring System

Self-hosted platform for monitoring email addresses, phone numbers, and usernames of family members against breach databases and data exposure sources. Serves as a proof-of-concept for lightweight SMB security monitoring tools.

## Problem / Motivation
Individuals and families lack affordable, private alternatives to paid services like Have I Been Pwned or dark web monitoring tools. This project creates a personal, extensible system that can later scale toward the cybersafe-smb initiative.

## Proposed Solution
Build a Dockerized application that periodically checks family details against HIBP, XposedOrNot, and other open sources. Include a simple dashboard and email/SMS notifications for new exposures.

## Tech Stack Suggestions
- Backend: Python (FastAPI or Flask)
- Database: SQLite or PostgreSQL
- Orchestration: Docker Compose + cron/scheduler
- Notifications: SMTP or Twilio
- Frontend: Streamlit or basic React

## Feasibility / Challenges
- Rate limiting on public breach APIs
- Secure storage of personal identifiable information
- Balancing comprehensiveness with privacy

## Next Steps / Milestones
1. Set up core HIBP integration script
2. Implement family member data model and secure storage
3. Build notification engine and basic dashboard
4. Containerize and document deployment