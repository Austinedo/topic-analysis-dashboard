> Using the selected TF-IDF configuration, K-Means divided the negative reviews into **six clusters**. The table below contains every reported high-weighted term for each cluster.

#### < Review Clustering Results >

| Cluster | Highest-weighted terms (top-25 terms) | Possible pattern |
|---|---|---|
| 1 | `hair`, `cut`, `cut hair`, `hair cut`, `stylist`, `asked`, `like`, `lady`, `haircut`, `wanted`, `short`, `know`, `want`, `place`, `going`, `guy`, `worst`, `horrible`, `didnt`, `location`, `time`, `uneven`, `bad`, `job`, `experience` | Unsatisfactory haircut outcomes, including uneven cuts and dissatisfaction with the stylist's work |
| 2 | `X`, `X`, `X`, `experience`, `hairtime`, `cut`, `went`, `location`, `stylist`, `going`, `got`, `haircut`, `store`, `left`, `said`, `bad`, `took`, `terrible`, `told`, `minutes`, `dont`, `worst`, `like`, `barber` | Complaints connected to a specific visit or location, often mentioning haircuts, service timing, and negative experiences |
| 3 | `haircut`, `worst`, `worst haircut`, `bad`, `experience`, `guy`, `stylist`, `location`, `wanted`, `asked`, `like`, `place`, `good`, `hair`, `ive`, `people`, `got`, `time`, `going`, `fast`, `coming`, `didnt`, `customers`, `head`, `great` | Poor haircut experiences and unmet styling requests |
| 4 | `service`, `bad`, `customer service`, `customer`, `haircut`, `told`, `asked`, `place`, `hair`, `rude worst`, `terrible`, `time`, `want`, `horribleonline`, `good`, `cut`, `check`, `likesaid`, `barber`, `experience`, `recommend`, `minutes` | Customer-service complaints, including poor treatment and negative appointment experiences |
| 5 | `staff`, `rude`, `haircuts`, `haircut`, `experience`, `location`, `customers`, `bad`, `listen`, `worst`, `saying`, `place`, `went`, `working`, `customer`, `salon`, `dont`, `unprofessional`, `left`, `wait`, `recommend`, `got`, `coming`, `store`, `want` | Rude or unprofessional staff behavior, poor communication, and concerns that may lead customers not to return |
| 6 | `wait`, `place`, `good`, `time`, `haircuts`, `dont`, `people`, `lady`, `online`, `minutes`, `bad`, `stylist`, `like`, `horrible`, `cut`, `nice`, `asked`, `away`, `going`, `experience`, `close`, `man`, `woman`, `haircut`, `guy` | Waiting-time and appointment-process concerns, with related mentions of stylists and haircut quality |

#### < Interpretation >

> The six clusters suggest recurring concerns involving haircut outcomes, customer service, staff behavior, and waiting. However, they do not form clean, distinct topics. Terms such as `haircut`, `bad`, `worst`, `experience`, `service`, and `stylist` recur across several clusters, while some extracted terms are n-grams introduced during preprocessing.
>
> This overlap indicates that TF-IDF K-Means captures shared complaint vocabulary more than separate underlying themes. Individual reviews can describe an uneven haircut, a long wait, and rude staff together, while different reviewers may use different wording for the same concern.
>
> The six-cluster result is therefore best treated as an exploratory baseline: it surfaces broad and recognizable complaint patterns, but does not provide clearly separated or semantically coherent topics.