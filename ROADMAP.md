# OrbiHub Development Roadmap

## Vision
Transform OrbiHub from a local desktop marketplace into a scalable, cloud-enabled platform for rocketry teams with secure workspace isolation for sensitive flight data.

---

# OrbiHub Development Roadmap

## 🎯 Current Focus (December 2025)

**Sprint:** QThread Implementation + App Launching  
**Target:** December 22, 2025 - Phase 1 Release (v1.0)

### This Week (Dec 13-20)
- [ ] Implement `InstallWorker(QThread)` for non-blocking installation
- [ ] Create `orbihub/ui/workers.py` with worker classes
- [ ] Update `handle_install()` to use worker thread with signals
- [ ] Animated progress bar during git clone/venv/pip install
- [ ] Test installation on all platforms (Mac/Windows/Linux)
- [ ] Implement `launch_app()` - detect app type, run with subprocess
- [ ] Change Install → Launch button for installed apps

### Next Week (Dec 21-27)
- [ ] PyInstaller `.spec` file configuration
- [ ] Bundle assets with executable
- [ ] Update `paths.py` for PyInstaller compatibility (`sys._MEIPASS`)
- [ ] Build and test executable on clean machines
- [ ] Fix any missing dependencies/assets issues

### Week of Dec 30
- [ ] Write user documentation (installation, usage, troubleshooting)
- [ ] Create `docs/APP_DEVELOPER.md` guide
- [ ] Beta testing with FIU SEDS team (3-5 members)
- [ ] Bug fixes and polish based on feedback
- [ ] **Release v1.0 - December 22, 2026**

**NOTE**: would like to release sooner so V.1 can be completed
---

## Phase 1: Local Foundation (Current - January 2026)
**Goal:** Stable local desktop application with SQLite backend

### Features
- [X] PyQt6 desktop interface with aerospace theme
- [X] Local SQLite database for installed apps
- [X] Virtual environment management per app (venv + pip)
- [X] Browse rocketry tools (app cards with images, descriptions)
- [X] Cross-platform support (Windows, macOS, Linux)
- [X] Uninstall functionality (Settings button → delete files + DB record)
- [X] About dialog (display app metadata)
- [ ] **Install with QThread (non-blocking UI)** ⏳ IN PROGRESS
- [ ] **App launching capability** ⏳ IN PROGRESS
- [ ] App dependency resolution (requirements.txt → pip install)
- [ ] Automatic updates check (v1.1 feature)
- [X] Basic error handling and logging (file + console)

### Current Status (Dec 13, 2025)
**Working:**
- ✅ UI displays app cards from registry
- ✅ About button shows app information dialog
- ✅ Settings button uninstalls apps (delete folder + database cleanup)
- ✅ Database tracks installed apps with timestamps
- ✅ Logging system (file: `~/.orbihub/logs/orbihub.log` + console)
- ✅ App installation function (blocks UI - needs QThread)

**In Progress:**
- 🚧 QThread implementation for non-blocking installation
- 🚧 Progress bar animation during install
- 🚧 App launching (subprocess to run installed apps)

**Blocked/Waiting:**
- ⏸️ Dynamic registry (needs Phase 2 backend API)
- ⏸️ Search functionality (waiting for more apps)
- ⏸️ Update checking (needs version comparison logic)

### Technical Stack
- **Frontend:** PyQt6 (desktop UI)
- **Database:** SQLite (local file at `~/.orbihub/orbihub.db`)
- **Package Management:** venv (virtual environments), pip
- **Version Control:** Git (for app installation)
- **Distribution:** PyInstaller (standalone executables)
- **Logging:** Python logging module (file + console handlers)

### Success Criteria
- [x] 10+ FIU SEDS members actively using OrbiHub
- [ ] 5+ apps available in local catalog (currently 3 hardcoded)
- [ ] Stable installation/uninstallation workflow
- [ ] Zero critical bugs in production use
- [ ] Executable builds for macOS and Windows

---

## Phase 2: Central App Repository (Q1-Q2 2026)
**Goal:** Shared app catalog with centralized metadata, while keeping installations local

### Features
- [ ] REST API backend for app catalog
- [ ] PostgreSQL database for app metadata
- [ ] App submission/review workflow
- [ ] Version management (semantic versioning)
- [ ] App ratings and reviews
- [ ] Search and filtering improvements
- [ ] Automatic update notifications
- [ ] Usage analytics (anonymous, aggregated)

### Architecture
```
Desktop Client (PyQt6)
    ├── Local SQLite (installed apps, user prefs)
    └── HTTP → REST API
                └── PostgreSQL (app catalog, metadata, reviews)
```

### Technical Stack
- **Backend API:** FastAPI or Flask
- **Database:** PostgreSQL (hosted on Railway/Supabase/Render)
- **Authentication:** JWT tokens (for app submission)
- **Deployment:** Docker containers

### API Endpoints (Examples)
```
GET  /api/apps                    # List all apps
GET  /api/apps/{app_id}           # Get app details
POST /api/apps                    # Submit new app (authenticated)
GET  /api/apps/{app_id}/versions  # Get version history
POST /api/reviews                 # Submit review
GET  /api/search?q=telemetry      # Search apps
```

### Success Criteria
- Central catalog accessible to all FIU SEDS members
- App developers can submit/update their tools
- Automatic version checking works reliably

---

## Phase 3: Workspace Isolation (Q4 2026 - Q1 2027)
**Goal:** Secure, team-based workspaces for sensitive flight data and proprietary tools

### Critical Security Requirement
**Flight data and proprietary avionics tools CANNOT be publicly accessible**
- Competition data (IREC, SA Cup, etc.)
- Custom flight computer code
- Telemetry logs and analysis
- Sensor calibration data
- Team-specific configurations

### Workspace Features

#### 3.1 Workspace Architecture
- [ ] **Organizations/Teams:** FIU SEDS, other university teams, companies
- [ ] **Role-Based Access Control (RBAC)**
  - Owner (full control)
  - Admin (manage members, apps)
  - Developer (publish apps to workspace)
  - Member (install workspace apps)
  - Guest (read-only, limited access)
- [ ] **Workspace Types:**
  - **Public Workspace:** Free, open app catalog (community tools)
  - **Private Workspace:** Team-only, invite-based (flight data tools)
  - **Enterprise Workspace:** For companies (paid tier)

#### 3.2 Data Isolation
```
PostgreSQL Schema Design:

public_apps (public)
    ├── id, name, version, repo_url
    └── publicly visible

workspaces (isolated)
    ├── workspace_id (UUID)
    ├── name (e.g., "FIU SEDS Avionics")
    ├── type (public/private/enterprise)
    └── created_by

workspace_members
    ├── workspace_id
    ├── user_id
    ├── role (owner/admin/developer/member)
    └── invited_at

workspace_apps (private)
    ├── id, workspace_id
    ├── app_id, name, version
    ├── is_public (bool - can share outside workspace?)
    └── Only visible to workspace members

flight_data (highly restricted)
    ├── workspace_id
    ├── flight_id, mission_name
    ├── telemetry_logs (encrypted?)
    ├── sensor_data
    └── access_log (audit trail)
```

#### 3.3 Authentication & Authorization
- [ ] User accounts (email/password + OAuth providers)
- [ ] Workspace invitations (email-based)
- [ ] API keys for programmatic access
- [ ] Session management (JWT with refresh tokens)
- [ ] Two-factor authentication (optional, recommended for enterprise)

#### 3.4 Desktop Client Updates
- [ ] Workspace selector on login
- [ ] Install apps from multiple workspaces
- [ ] Clear visual indication of app source (public vs workspace)
- [ ] Workspace-specific settings and configurations
- [ ] Sync flight data to workspace (optional, encrypted)

### Example User Flows

**Flow 1: FIU SEDS Member Installing Flight Computer Configurator**
1. Opens OrbiHub, logs in
2. Selects "FIU SEDS Avionics" workspace
3. Browses private apps (Orizaba Flight Computer Config, Telemetry Analyzer)
4. Installs app (only accessible to FIU SEDS members)
5. App stores config locally, optionally syncs to workspace cloud storage

**Flow 2: Public Community Tool**
1. User browses Public Workspace
2. Finds "OpenRocket Plugin Manager" (open-source)
3. Installs to local machine
4. No authentication required for public tools

**Flow 3: App Developer Publishing to Workspace**
1. Developer creates new flight data analysis tool
2. Logs into OrbiHub Developer Portal
3. Selects "FIU SEDS Avionics" workspace
4. Uploads app package, sets version, adds description
5. App published to workspace (requires admin approval)
6. Team members get update notification

### Security Considerations
- [ ] End-to-end encryption for sensitive flight data
- [ ] Audit logs (who accessed what, when)
- [ ] IP whitelisting for enterprise workspaces
- [ ] Data retention policies
- [ ] GDPR/privacy compliance (if scaling beyond university)
- [ ] Rate limiting on API endpoints
- [ ] Input validation and SQL injection prevention

### Success Criteria
- FIU SEDS can securely share proprietary tools within team
- Flight data remains confidential to workspace members
- Easy onboarding for new team members
- No data leaks or unauthorized access

---

## Phase 4: Advanced Features (2027+)
**Goal:** Production-ready platform with enterprise capabilities

### Features
- [ ] **CI/CD Integration:** Auto-deploy apps from GitHub releases
- [ ] **App Sandboxing:** Containerized app execution (security)
- [ ] **Cloud Storage:** Workspace file storage (flight logs, configs)
- [ ] **Real-time Collaboration:** Shared flight data analysis sessions
- [ ] **Telemetry Streaming:** Live telemetry viewer (WebSockets)
- [ ] **Mobile Companion App:** View flight data on mobile
- [ ] **Marketplace Monetization:** Paid apps/plugins (revenue share)
- [ ] **Plugin System:** Extend OrbiHub functionality
- [ ] **Multi-language Support:** i18n for global teams
- [ ] **Advanced Analytics:** Workspace usage insights, app performance

### Potential Integrations
- **GitHub/GitLab:** Auto-publish apps from releases
- **Discord/Slack:** Notifications for app updates, flight events
- **AWS S3/GCS:** Cloud storage for large flight data files
- **Stripe:** Payment processing for enterprise workspaces
- **OpenTelemetry:** App performance monitoring

---

## Technical Evolution

### Infrastructure Progression
```
Phase 1: Local SQLite
    └── No hosting costs, simple deployment

Phase 2: Hybrid (Local + Cloud)
    ├── SQLite: installed apps, user prefs (local)
    └── PostgreSQL: app catalog (cloud - Railway/Supabase)

Phase 3: Multi-tenant Cloud
    ├── SQLite: installed apps (local)
    ├── PostgreSQL: workspaces, apps, users (cloud)
    └── Object Storage: flight data files (S3/GCS)

Phase 4: Fully Distributed
    ├── CDN: app distribution (CloudFlare)
    ├── Kubernetes: scalable API backend
    ├── Redis: caching, session management
    └── Message Queue: async jobs (Celery/RabbitMQ)
```

### Database Schema Evolution
```sql
-- Phase 1: Local SQLite
installed_apps (id, app_id, name, version, installed_at)

-- Phase 2: PostgreSQL App Catalog
public_apps (id, app_id, name, version, repo_url, downloads, rating)
reviews (id, app_id, user_id, rating, comment, created_at)

-- Phase 3: Workspaces + RBAC
workspaces (id, name, type, owner_id, created_at)
workspace_members (workspace_id, user_id, role, invited_at)
workspace_apps (id, workspace_id, app_id, is_public, created_at)
users (id, email, password_hash, created_at)

-- Phase 4: Full Platform
app_versions (id, app_id, version, changelog, release_date)
telemetry_sessions (id, workspace_id, flight_id, start_time, end_time)
audit_logs (id, user_id, action, resource, timestamp)
billing (workspace_id, plan, stripe_customer_id, next_billing_date)
```

---

## Deployment Strategy

### Phase 2-3: Managed Services (Low Maintenance)
- **Database:** Supabase (PostgreSQL + Auth + Storage in one)
- **Backend API:** Railway or Render (auto-deploy from Git)
- **File Storage:** Supabase Storage or AWS S3
- **Monitoring:** Sentry (error tracking)

**Monthly Costs (Estimated):**
- Supabase Free Tier: $0 (500MB database, 1GB storage)
- Railway Hobby: $5/month (shared resources)
- Total: ~$5-10/month for Phase 2-3

### Phase 4: Production Scale
- **Kubernetes (GKE/EKS):** Auto-scaling backend
- **PostgreSQL:** Managed instance (AWS RDS, $50-200/mo)
- **CDN:** CloudFlare (free tier or $20/mo)
- **Monitoring:** DataDog (you know this one! 😄)
- Total: ~$100-300/month depending on usage

---

## Key Milestones & Timeline

| Phase | Timeline | Key Deliverable |
|-------|----------|-----------------|
| **Phase 1** | Now - Q1 2026 | Local OrbiHub with 5+ apps, FIU SEDS adoption |
| **Phase 2** | Q2-Q3 2026 | Central app catalog, 20+ apps, update system |
| **Phase 3** | Q4 2026 - Q1 2027 | Workspace isolation, 3+ university teams using private workspaces |
| **Phase 4** | 2027+ | Enterprise-ready platform, mobile app, monetization |

---

## Why This Matters

###  (Career)
- **Full-stack experience:** Desktop (PyQt6) → Backend (FastAPI) → Database (PostgreSQL) → Cloud (AWS/GCP)
- **Distributed systems:** Multi-tenant architecture, workspace isolation, data security
- **Real users:** FIU SEDS team, other rocketry clubs
- **Interview story:** "I built a platform that scaled from local SQLite to multi-workspace cloud architecture serving X teams"
- **Relevant to targets:** DataDog (monitoring), Varda Space (aerospace tooling), Google/Microsoft (cloud platforms)

### For FIU SEDS
- **Secure collaboration:** Share proprietary tools without leaking to competitors
- **Onboarding:** New members get instant access to team tools
- **Knowledge preservation:** Tools and data persist beyond graduation cycles
- **Competition edge:** Custom flight analysis tools stay internal

### For Rocketry Community
- **Open-source hub:** Public workspace for community tools
- **Standardization:** Common platform for telemetry, analysis, simulation
- **Cross-team collaboration:** Teams can choose to share non-sensitive tools

---

## Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| **Data breach (flight data leak)** | Encryption at rest/transit, audit logs, regular security audits |
| **Scope creep (over-engineering)** | Strict phase gates, MVP mindset, user feedback loops |
| **Hosting costs** | Start with free tiers, scale based on actual usage |
| **User adoption** | Focus on FIU SEDS first, prove value before expanding |
| **Maintenance burden** | Automated testing, CI/CD, managed services over self-hosting |
| **Competition (existing tools)** | Niche focus on rocketry, workspace isolation as differentiator |

---

## Success Metrics

### Phase 1
- [ ] 10+ FIU SEDS members actively using OrbiHub
- [ ] 5+ apps in local catalog
- [ ] Zero critical bugs in production use

### Phase 2
- 🎯 50+ users across multiple teams
- 🎯 20+ apps in central catalog
- 🎯 90%+ uptime on API backend

### Phase 3
- 🎯 3+ university teams with private workspaces
- 🎯 100% of sensitive flight data isolated to workspaces
- 🎯 Zero unauthorized data access incidents

### Phase 4
- 🎯 500+ users, 10+ organizations
- 🎯 Revenue-positive (enterprise subscriptions)
- 🎯 Mobile app with 1000+ downloads

---

## Next Steps (Immediate)

1. **Finish Phase 1 MVP** (focus on this first!)
   - [ ] Complete installation system
   - [ ] Add 5 apps to local catalog
   - [ ] Get feedback from FIU SEDS team
   - [ ] Document setup/usage

2. **Plan Phase 2 Architecture**
   - [ ] Design REST API endpoints
   - [ ] Choose hosting provider (Supabase vs Railway)
   - [ ] Create PostgreSQL schema for app catalog
   - [ ] Write migration plan (SQLite → PostgreSQL)

3. **Explore Authentication**
   - [ ] Research Supabase Auth vs custom JWT
   - [ ] Design user model (email, OAuth, API keys)

4. **Security Research**
   - [ ] Study multi-tenant database patterns (Row-Level Security in PostgreSQL)
   - [ ] Plan encryption strategy for flight data
   - [ ] Review OWASP guidelines for web APIs

---

## Resources & Learning

### Technologies to Learn
- **FastAPI:** Modern Python web framework (if not already familiar)
- **PostgreSQL Advanced:** Row-level security, partitioning, indexing
- **Docker:** Containerization for deployment
- **Auth0/Supabase Auth:** User authentication best practices
- **AWS S3/GCS:** Object storage for large files

### Inspiration (Similar Platforms)
- **npm/PyPI:** Package management models
- **GitHub Packages:** Workspace-scoped packages
- **Docker Hub:** Public vs private registries
- **Slack/Discord:** Workspace isolation patterns
- **Notion:** Multi-workspace collaboration

---

## Open Questions (To Decide Later)

1. **Licensing:** Open-source core + paid enterprise features? Fully open? Fully proprietary?
2. **App distribution:** Git repos only? Support binary uploads? App store model?
3. **Telemetry privacy:** Opt-in usage analytics? Fully anonymous? No tracking?
4. **Monetization:** Free for universities, paid for companies? Freemium model? Donations?
5. **Mobile app:** React Native? Flutter? Native iOS/Android? Worth the effort?
6. **Integration scope:** How deep to integrate with existing tools (OpenRocket, RASAero)?

---

*Last Updated: November 18, 2025*
*Maintainer: Eriel, Tomas*
*Status: Phase 1 (In Progress)*
