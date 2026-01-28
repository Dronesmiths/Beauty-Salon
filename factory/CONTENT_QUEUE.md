# Beauty Salon: Content & Newsletter Queue

Use this checklist to track the rollout of the 50 high-authority content pieces. Mark as `[x]` only after the page is live and CloudFront cache is invalidated.

## Phase 1: The Authority Foundation (1-10)
- [x] **01: Cornerstone Guide** - Welcome to Beauty Salon: Antelope Valley's Premier Beauty Destination
- [x] **02: Trends Analysis** - Top Hair Color Trends Taking Over 2026
- [x] **03: Service Deep Dive** - Why Monthly Facials Are More Than Just a Treat
- [x] **04: Locality Anchor** - Why We Are Voted Best Balayage in Palmdale
- [x] **05: Locality Anchor** - Wedding Makeup Tips for Lancaster Brides
- [x] **06: Locality Anchor** - Why Quartz Hill Locals Love Our Hydrafacials
- [ ] **07: Pro Tip** - Summer Hair Care Tips for High Desert Heat
- [ ] **08: Service Comparison** - Lash Extensions vs. Lash Lifts: Which is Right for You?
- [ ] **09: Locality Anchor** - Best Acne Treatments in Palmdale
- [ ] **10: Seasonal** - Holiday Glam Looks: Book Early for Your Event

## Phase 2: Strategic Expansion (11-30)
- [ ] **11: Locality Anchor** - Mobile Bridal Services in Rosamond & Leona Valley
- [ ] **12: PAA Capture** - How often should I get a haircut to maintain length?
- [ ] **13: Service Deep Dive** - Chemical Peels: Debunking the Myths
- [ ] **14: Project Spotlight** - From Box Dye Correction to Golden Blonde
- [ ] **15: Cornerstone Pillar** - The Ultimate Guide to Skincare Routines for Dry Desert Air
- [ ] **16-30:** ...

## Phase 3: Domain Dominance (31-50)
- [ ] **31:** ...
- [ ] **50:** ...

> [!IMPORTANT]
> **Deployment Rule**: Every time a checkbox is marked `[x]`, you must:
> 1. Sync the repo: `git add . && git commit -m "feat: deploy content piece #[XX]" && git push`
> 2. Sync S3: `aws s3 sync . s3://[BUCKET] --profile mediusa`
> 3. Invalidate: `aws cloudfront create-invalidation --distribution-id [ID] --paths "/news/*" "/blog/*"`
