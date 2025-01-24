import types
from email.generator import BytesGenerator
from typing import Any, Protocol, TypeVar, overload

import google.auth.credentials
import httplib2
import oauth2client  # type: ignore[import-not-found]
from _typeshed import Incomplete
from google.api_core.client_options import ClientOptions
from typing_extensions import Literal

import googleapiclient._apis.abusiveexperiencereport.v1
import googleapiclient._apis.acceleratedmobilepageurl.v1
import googleapiclient._apis.accessapproval.v1
import googleapiclient._apis.accesscontextmanager.v1
import googleapiclient._apis.accesscontextmanager.v1beta
import googleapiclient._apis.acmedns.v1
import googleapiclient._apis.addressvalidation.v1
import googleapiclient._apis.adexchangebuyer.v1_2
import googleapiclient._apis.adexchangebuyer.v1_3
import googleapiclient._apis.adexchangebuyer.v1_4
import googleapiclient._apis.adexchangebuyer2.v2beta1
import googleapiclient._apis.adexperiencereport.v1
import googleapiclient._apis.admin.datatransfer_v1
import googleapiclient._apis.admin.directory_v1
import googleapiclient._apis.admin.reports_v1
import googleapiclient._apis.admob.v1
import googleapiclient._apis.admob.v1beta
import googleapiclient._apis.adsense.v2
import googleapiclient._apis.adsensehost.v4_1
import googleapiclient._apis.adsenseplatform.v1
import googleapiclient._apis.adsenseplatform.v1alpha
import googleapiclient._apis.advisorynotifications.v1
import googleapiclient._apis.aiplatform.v1
import googleapiclient._apis.aiplatform.v1beta1
import googleapiclient._apis.airquality.v1
import googleapiclient._apis.alertcenter.v1beta1
import googleapiclient._apis.alloydb.v1
import googleapiclient._apis.alloydb.v1alpha
import googleapiclient._apis.alloydb.v1beta
import googleapiclient._apis.analytics.v3
import googleapiclient._apis.analyticsadmin.v1alpha
import googleapiclient._apis.analyticsadmin.v1beta
import googleapiclient._apis.analyticsdata.v1alpha
import googleapiclient._apis.analyticsdata.v1beta
import googleapiclient._apis.analyticshub.v1
import googleapiclient._apis.analyticshub.v1beta1
import googleapiclient._apis.analyticsreporting.v4
import googleapiclient._apis.androiddeviceprovisioning.v1
import googleapiclient._apis.androidenterprise.v1
import googleapiclient._apis.androidmanagement.v1
import googleapiclient._apis.androidpublisher.v3
import googleapiclient._apis.apigateway.v1
import googleapiclient._apis.apigateway.v1beta
import googleapiclient._apis.apigee.v1
import googleapiclient._apis.apigeeregistry.v1
import googleapiclient._apis.apikeys.v2
import googleapiclient._apis.apim.v1alpha
import googleapiclient._apis.appengine.v1
import googleapiclient._apis.appengine.v1alpha
import googleapiclient._apis.appengine.v1beta
import googleapiclient._apis.appengine.v1beta4
import googleapiclient._apis.appengine.v1beta5
import googleapiclient._apis.apphub.v1
import googleapiclient._apis.apphub.v1alpha
import googleapiclient._apis.area120tables.v1alpha1
import googleapiclient._apis.areainsights.v1
import googleapiclient._apis.artifactregistry.v1
import googleapiclient._apis.artifactregistry.v1beta1
import googleapiclient._apis.artifactregistry.v1beta2
import googleapiclient._apis.assuredworkloads.v1
import googleapiclient._apis.assuredworkloads.v1beta1
import googleapiclient._apis.authorizedbuyersmarketplace.v1
import googleapiclient._apis.authorizedbuyersmarketplace.v1alpha
import googleapiclient._apis.backupdr.v1
import googleapiclient._apis.baremetalsolution.v1
import googleapiclient._apis.baremetalsolution.v1alpha1
import googleapiclient._apis.baremetalsolution.v2
import googleapiclient._apis.batch.v1
import googleapiclient._apis.beyondcorp.v1
import googleapiclient._apis.beyondcorp.v1alpha
import googleapiclient._apis.biglake.v1
import googleapiclient._apis.bigquery.v2
import googleapiclient._apis.bigqueryconnection.v1
import googleapiclient._apis.bigqueryconnection.v1beta1
import googleapiclient._apis.bigquerydatapolicy.v1
import googleapiclient._apis.bigquerydatatransfer.v1
import googleapiclient._apis.bigqueryreservation.v1
import googleapiclient._apis.bigqueryreservation.v1alpha2
import googleapiclient._apis.bigqueryreservation.v1beta1
import googleapiclient._apis.bigtableadmin.v1
import googleapiclient._apis.bigtableadmin.v2
import googleapiclient._apis.billingbudgets.v1
import googleapiclient._apis.billingbudgets.v1beta1
import googleapiclient._apis.binaryauthorization.v1
import googleapiclient._apis.binaryauthorization.v1beta1
import googleapiclient._apis.blockchainnodeengine.v1
import googleapiclient._apis.blogger.v2
import googleapiclient._apis.blogger.v3
import googleapiclient._apis.books.v1
import googleapiclient._apis.businessprofileperformance.v1
import googleapiclient._apis.calendar.v3
import googleapiclient._apis.certificatemanager.v1
import googleapiclient._apis.chat.v1
import googleapiclient._apis.checks.v1alpha
import googleapiclient._apis.chromemanagement.v1
import googleapiclient._apis.chromepolicy.v1
import googleapiclient._apis.chromeuxreport.v1
import googleapiclient._apis.civicinfo.v2
import googleapiclient._apis.classroom.v1
import googleapiclient._apis.cloudasset.v1
import googleapiclient._apis.cloudasset.v1beta1
import googleapiclient._apis.cloudasset.v1p1beta1
import googleapiclient._apis.cloudasset.v1p4beta1
import googleapiclient._apis.cloudasset.v1p5beta1
import googleapiclient._apis.cloudasset.v1p7beta1
import googleapiclient._apis.cloudbilling.v1
import googleapiclient._apis.cloudbilling.v1beta
import googleapiclient._apis.cloudbuild.v1
import googleapiclient._apis.cloudbuild.v1alpha1
import googleapiclient._apis.cloudbuild.v1alpha2
import googleapiclient._apis.cloudbuild.v1beta1
import googleapiclient._apis.cloudbuild.v2
import googleapiclient._apis.cloudchannel.v1
import googleapiclient._apis.cloudcommerceprocurement.v1
import googleapiclient._apis.cloudcontrolspartner.v1
import googleapiclient._apis.cloudcontrolspartner.v1beta
import googleapiclient._apis.clouddebugger.v2
import googleapiclient._apis.clouddeploy.v1
import googleapiclient._apis.clouderrorreporting.v1beta1
import googleapiclient._apis.cloudfunctions.v1
import googleapiclient._apis.cloudfunctions.v2
import googleapiclient._apis.cloudfunctions.v2alpha
import googleapiclient._apis.cloudfunctions.v2beta
import googleapiclient._apis.cloudidentity.v1
import googleapiclient._apis.cloudidentity.v1beta1
import googleapiclient._apis.cloudiot.v1
import googleapiclient._apis.cloudkms.v1
import googleapiclient._apis.cloudprofiler.v2
import googleapiclient._apis.cloudresourcemanager.v1
import googleapiclient._apis.cloudresourcemanager.v1beta1
import googleapiclient._apis.cloudresourcemanager.v2
import googleapiclient._apis.cloudresourcemanager.v2beta1
import googleapiclient._apis.cloudresourcemanager.v3
import googleapiclient._apis.cloudscheduler.v1
import googleapiclient._apis.cloudscheduler.v1beta1
import googleapiclient._apis.cloudsearch.v1
import googleapiclient._apis.cloudshell.v1
import googleapiclient._apis.cloudshell.v1alpha1
import googleapiclient._apis.cloudsupport.v2
import googleapiclient._apis.cloudsupport.v2beta
import googleapiclient._apis.cloudtasks.v2
import googleapiclient._apis.cloudtasks.v2beta2
import googleapiclient._apis.cloudtasks.v2beta3
import googleapiclient._apis.cloudtrace.v1
import googleapiclient._apis.cloudtrace.v2
import googleapiclient._apis.cloudtrace.v2beta1
import googleapiclient._apis.composer.v1
import googleapiclient._apis.composer.v1beta1
import googleapiclient._apis.compute.alpha
import googleapiclient._apis.compute.beta
import googleapiclient._apis.compute.v1
import googleapiclient._apis.config.v1
import googleapiclient._apis.connectors.v1
import googleapiclient._apis.connectors.v2
import googleapiclient._apis.contactcenteraiplatform.v1alpha1
import googleapiclient._apis.contactcenterinsights.v1
import googleapiclient._apis.container.v1
import googleapiclient._apis.container.v1beta1
import googleapiclient._apis.containeranalysis.v1
import googleapiclient._apis.containeranalysis.v1alpha1
import googleapiclient._apis.containeranalysis.v1beta1
import googleapiclient._apis.content.v2
import googleapiclient._apis.content.v2_1
import googleapiclient._apis.contentwarehouse.v1
import googleapiclient._apis.css.v1
import googleapiclient._apis.customsearch.v1
import googleapiclient._apis.datacatalog.v1
import googleapiclient._apis.datacatalog.v1beta1
import googleapiclient._apis.dataflow.v1b3
import googleapiclient._apis.dataform.v1beta1
import googleapiclient._apis.datafusion.v1
import googleapiclient._apis.datafusion.v1beta1
import googleapiclient._apis.datalabeling.v1beta1
import googleapiclient._apis.datalineage.v1
import googleapiclient._apis.datamigration.v1
import googleapiclient._apis.datamigration.v1beta1
import googleapiclient._apis.datapipelines.v1
import googleapiclient._apis.dataplex.v1
import googleapiclient._apis.dataportability.v1
import googleapiclient._apis.dataportability.v1beta
import googleapiclient._apis.dataproc.v1
import googleapiclient._apis.dataproc.v1beta2
import googleapiclient._apis.datastore.v1
import googleapiclient._apis.datastore.v1beta1
import googleapiclient._apis.datastore.v1beta3
import googleapiclient._apis.datastream.v1
import googleapiclient._apis.datastream.v1alpha1
import googleapiclient._apis.deploymentmanager.alpha
import googleapiclient._apis.deploymentmanager.v2
import googleapiclient._apis.deploymentmanager.v2beta
import googleapiclient._apis.developerconnect.v1
import googleapiclient._apis.dfareporting.v3_3
import googleapiclient._apis.dfareporting.v3_4
import googleapiclient._apis.dfareporting.v3_5
import googleapiclient._apis.dfareporting.v4
import googleapiclient._apis.dialogflow.v2
import googleapiclient._apis.dialogflow.v2beta1
import googleapiclient._apis.dialogflow.v3
import googleapiclient._apis.dialogflow.v3beta1
import googleapiclient._apis.digitalassetlinks.v1
import googleapiclient._apis.discovery.v1
import googleapiclient._apis.discoveryengine.v1
import googleapiclient._apis.discoveryengine.v1alpha
import googleapiclient._apis.discoveryengine.v1beta
import googleapiclient._apis.displayvideo.v1
import googleapiclient._apis.displayvideo.v2
import googleapiclient._apis.displayvideo.v3
import googleapiclient._apis.displayvideo.v4
import googleapiclient._apis.dlp.v2
import googleapiclient._apis.dns.v1
import googleapiclient._apis.dns.v1beta2
import googleapiclient._apis.dns.v2
import googleapiclient._apis.docs.v1
import googleapiclient._apis.documentai.v1
import googleapiclient._apis.documentai.v1beta2
import googleapiclient._apis.documentai.v1beta3
import googleapiclient._apis.domains.v1
import googleapiclient._apis.domains.v1alpha2
import googleapiclient._apis.domains.v1beta1
import googleapiclient._apis.domainsrdap.v1
import googleapiclient._apis.doubleclickbidmanager.v1
import googleapiclient._apis.doubleclickbidmanager.v1_1
import googleapiclient._apis.doubleclickbidmanager.v2
import googleapiclient._apis.doubleclicksearch.v2
import googleapiclient._apis.drive.v2
import googleapiclient._apis.drive.v3
import googleapiclient._apis.driveactivity.v2
import googleapiclient._apis.drivelabels.v2
import googleapiclient._apis.drivelabels.v2beta
import googleapiclient._apis.essentialcontacts.v1
import googleapiclient._apis.eventarc.v1
import googleapiclient._apis.eventarc.v1beta1
import googleapiclient._apis.factchecktools.v1alpha1
import googleapiclient._apis.fcm.v1
import googleapiclient._apis.fcmdata.v1beta1
import googleapiclient._apis.file.v1
import googleapiclient._apis.file.v1beta1
import googleapiclient._apis.firebase.v1beta1
import googleapiclient._apis.firebaseappcheck.v1
import googleapiclient._apis.firebaseappcheck.v1beta
import googleapiclient._apis.firebaseappdistribution.v1
import googleapiclient._apis.firebaseappdistribution.v1alpha
import googleapiclient._apis.firebasedatabase.v1beta
import googleapiclient._apis.firebasedataconnect.v1beta
import googleapiclient._apis.firebasedynamiclinks.v1
import googleapiclient._apis.firebasehosting.v1
import googleapiclient._apis.firebasehosting.v1beta1
import googleapiclient._apis.firebaseml.v1
import googleapiclient._apis.firebaseml.v1beta2
import googleapiclient._apis.firebaseml.v2beta
import googleapiclient._apis.firebaserules.v1
import googleapiclient._apis.firebasestorage.v1beta
import googleapiclient._apis.firestore.v1
import googleapiclient._apis.firestore.v1beta1
import googleapiclient._apis.firestore.v1beta2
import googleapiclient._apis.fitness.v1
import googleapiclient._apis.forms.v1
import googleapiclient._apis.games.v1
import googleapiclient._apis.gamesConfiguration.v1configuration
import googleapiclient._apis.gameservices.v1
import googleapiclient._apis.gameservices.v1beta
import googleapiclient._apis.gamesManagement.v1management
import googleapiclient._apis.genomics.v1
import googleapiclient._apis.genomics.v1alpha2
import googleapiclient._apis.genomics.v2alpha1
import googleapiclient._apis.gkebackup.v1
import googleapiclient._apis.gkehub.v1
import googleapiclient._apis.gkehub.v1alpha
import googleapiclient._apis.gkehub.v1alpha2
import googleapiclient._apis.gkehub.v1beta
import googleapiclient._apis.gkehub.v1beta1
import googleapiclient._apis.gkehub.v2
import googleapiclient._apis.gkehub.v2alpha
import googleapiclient._apis.gkehub.v2beta
import googleapiclient._apis.gkeonprem.v1
import googleapiclient._apis.gmail.v1
import googleapiclient._apis.gmailpostmastertools.v1
import googleapiclient._apis.gmailpostmastertools.v1beta1
import googleapiclient._apis.groupsmigration.v1
import googleapiclient._apis.groupssettings.v1
import googleapiclient._apis.healthcare.v1
import googleapiclient._apis.healthcare.v1beta1
import googleapiclient._apis.homegraph.v1
import googleapiclient._apis.iam.v1
import googleapiclient._apis.iam.v2
import googleapiclient._apis.iam.v2beta
import googleapiclient._apis.iamcredentials.v1
import googleapiclient._apis.iap.v1
import googleapiclient._apis.iap.v1beta1
import googleapiclient._apis.ideahub.v1alpha
import googleapiclient._apis.ideahub.v1beta
import googleapiclient._apis.identitytoolkit.v1
import googleapiclient._apis.identitytoolkit.v2
import googleapiclient._apis.identitytoolkit.v3
import googleapiclient._apis.ids.v1
import googleapiclient._apis.indexing.v3
import googleapiclient._apis.integrations.v1
import googleapiclient._apis.integrations.v1alpha
import googleapiclient._apis.jobs.v2
import googleapiclient._apis.jobs.v3
import googleapiclient._apis.jobs.v3p1beta1
import googleapiclient._apis.jobs.v4
import googleapiclient._apis.keep.v1
import googleapiclient._apis.kgsearch.v1
import googleapiclient._apis.kmsinventory.v1
import googleapiclient._apis.language.v1
import googleapiclient._apis.language.v1beta1
import googleapiclient._apis.language.v1beta2
import googleapiclient._apis.language.v2
import googleapiclient._apis.libraryagent.v1
import googleapiclient._apis.licensing.v1
import googleapiclient._apis.lifesciences.v2beta
import googleapiclient._apis.localservices.v1
import googleapiclient._apis.logging.v2
import googleapiclient._apis.looker.v1
import googleapiclient._apis.managedidentities.v1
import googleapiclient._apis.managedidentities.v1alpha1
import googleapiclient._apis.managedidentities.v1beta1
import googleapiclient._apis.manufacturers.v1
import googleapiclient._apis.marketingplatformadmin.v1alpha
import googleapiclient._apis.meet.v2
import googleapiclient._apis.memcache.v1
import googleapiclient._apis.memcache.v1beta2
import googleapiclient._apis.merchantapi.accounts_v1beta
import googleapiclient._apis.merchantapi.conversions_v1beta
import googleapiclient._apis.merchantapi.datasources_v1beta
import googleapiclient._apis.merchantapi.inventories_v1beta
import googleapiclient._apis.merchantapi.lfp_v1beta
import googleapiclient._apis.merchantapi.notifications_v1beta
import googleapiclient._apis.merchantapi.products_v1beta
import googleapiclient._apis.merchantapi.promotions_v1beta
import googleapiclient._apis.merchantapi.quota_v1beta
import googleapiclient._apis.merchantapi.reports_v1beta
import googleapiclient._apis.merchantapi.reviews_v1beta
import googleapiclient._apis.metastore.v1
import googleapiclient._apis.metastore.v1alpha
import googleapiclient._apis.metastore.v1beta
import googleapiclient._apis.metastore.v2
import googleapiclient._apis.metastore.v2alpha
import googleapiclient._apis.metastore.v2beta
import googleapiclient._apis.migrationcenter.v1
import googleapiclient._apis.migrationcenter.v1alpha1
import googleapiclient._apis.ml.v1
import googleapiclient._apis.monitoring.v1
import googleapiclient._apis.monitoring.v3
import googleapiclient._apis.mybusinessaccountmanagement.v1
import googleapiclient._apis.mybusinessbusinesscalls.v1
import googleapiclient._apis.mybusinessbusinessinformation.v1
import googleapiclient._apis.mybusinesslodging.v1
import googleapiclient._apis.mybusinessnotifications.v1
import googleapiclient._apis.mybusinessplaceactions.v1
import googleapiclient._apis.mybusinessqanda.v1
import googleapiclient._apis.mybusinessverifications.v1
import googleapiclient._apis.netapp.v1
import googleapiclient._apis.netapp.v1beta1
import googleapiclient._apis.networkconnectivity.v1
import googleapiclient._apis.networkconnectivity.v1alpha1
import googleapiclient._apis.networkmanagement.v1
import googleapiclient._apis.networkmanagement.v1beta1
import googleapiclient._apis.networksecurity.v1
import googleapiclient._apis.networksecurity.v1beta1
import googleapiclient._apis.networkservices.v1
import googleapiclient._apis.networkservices.v1beta1
import googleapiclient._apis.notebooks.v1
import googleapiclient._apis.notebooks.v2
import googleapiclient._apis.oauth2.v2
import googleapiclient._apis.ondemandscanning.v1
import googleapiclient._apis.ondemandscanning.v1beta1
import googleapiclient._apis.oracledatabase.v1
import googleapiclient._apis.orgpolicy.v2
import googleapiclient._apis.osconfig.v1
import googleapiclient._apis.osconfig.v1alpha
import googleapiclient._apis.osconfig.v1beta
import googleapiclient._apis.osconfig.v2beta
import googleapiclient._apis.oslogin.v1
import googleapiclient._apis.oslogin.v1alpha
import googleapiclient._apis.oslogin.v1beta
import googleapiclient._apis.pagespeedonline.v5
import googleapiclient._apis.parallelstore.v1
import googleapiclient._apis.parallelstore.v1beta
import googleapiclient._apis.paymentsresellersubscription.v1
import googleapiclient._apis.people.v1
import googleapiclient._apis.places.v1
import googleapiclient._apis.playablelocations.v3
import googleapiclient._apis.playcustomapp.v1
import googleapiclient._apis.playdeveloperreporting.v1alpha1
import googleapiclient._apis.playdeveloperreporting.v1beta1
import googleapiclient._apis.playgrouping.v1alpha1
import googleapiclient._apis.playintegrity.v1
import googleapiclient._apis.policyanalyzer.v1
import googleapiclient._apis.policyanalyzer.v1beta1
import googleapiclient._apis.policysimulator.v1
import googleapiclient._apis.policysimulator.v1alpha
import googleapiclient._apis.policysimulator.v1beta
import googleapiclient._apis.policysimulator.v1beta1
import googleapiclient._apis.policytroubleshooter.v1
import googleapiclient._apis.policytroubleshooter.v1beta
import googleapiclient._apis.pollen.v1
import googleapiclient._apis.poly.v1
import googleapiclient._apis.privateca.v1
import googleapiclient._apis.privateca.v1beta1
import googleapiclient._apis.prod_tt_sasportal.v1alpha1
import googleapiclient._apis.publicca.v1
import googleapiclient._apis.publicca.v1alpha1
import googleapiclient._apis.publicca.v1beta1
import googleapiclient._apis.pubsub.v1
import googleapiclient._apis.pubsub.v1beta1a
import googleapiclient._apis.pubsub.v1beta2
import googleapiclient._apis.pubsublite.v1
import googleapiclient._apis.rapidmigrationassessment.v1
import googleapiclient._apis.readerrevenuesubscriptionlinking.v1
import googleapiclient._apis.realtimebidding.v1
import googleapiclient._apis.realtimebidding.v1alpha
import googleapiclient._apis.recaptchaenterprise.v1
import googleapiclient._apis.recommendationengine.v1beta1
import googleapiclient._apis.recommender.v1
import googleapiclient._apis.recommender.v1beta1
import googleapiclient._apis.redis.v1
import googleapiclient._apis.redis.v1beta1
import googleapiclient._apis.remotebuildexecution.v1
import googleapiclient._apis.remotebuildexecution.v1alpha
import googleapiclient._apis.remotebuildexecution.v2
import googleapiclient._apis.reseller.v1
import googleapiclient._apis.resourcesettings.v1
import googleapiclient._apis.retail.v2
import googleapiclient._apis.retail.v2alpha
import googleapiclient._apis.retail.v2beta
import googleapiclient._apis.run.v1
import googleapiclient._apis.run.v1alpha1
import googleapiclient._apis.run.v1beta1
import googleapiclient._apis.run.v2
import googleapiclient._apis.runtimeconfig.v1
import googleapiclient._apis.runtimeconfig.v1beta1
import googleapiclient._apis.safebrowsing.v4
import googleapiclient._apis.safebrowsing.v5
import googleapiclient._apis.sasportal.v1alpha1
import googleapiclient._apis.script.v1
import googleapiclient._apis.searchads360.v0
import googleapiclient._apis.searchconsole.v1
import googleapiclient._apis.secretmanager.v1
import googleapiclient._apis.secretmanager.v1beta1
import googleapiclient._apis.secretmanager.v1beta2
import googleapiclient._apis.securitycenter.v1
import googleapiclient._apis.securitycenter.v1beta1
import googleapiclient._apis.securitycenter.v1beta2
import googleapiclient._apis.securityposture.v1
import googleapiclient._apis.serviceconsumermanagement.v1
import googleapiclient._apis.serviceconsumermanagement.v1beta1
import googleapiclient._apis.servicecontrol.v1
import googleapiclient._apis.servicecontrol.v2
import googleapiclient._apis.servicedirectory.v1
import googleapiclient._apis.servicedirectory.v1beta1
import googleapiclient._apis.servicemanagement.v1
import googleapiclient._apis.servicenetworking.v1
import googleapiclient._apis.servicenetworking.v1beta
import googleapiclient._apis.serviceusage.v1
import googleapiclient._apis.serviceusage.v1beta1
import googleapiclient._apis.sheets.v4
import googleapiclient._apis.siteVerification.v1
import googleapiclient._apis.slides.v1
import googleapiclient._apis.smartdevicemanagement.v1
import googleapiclient._apis.solar.v1
import googleapiclient._apis.sourcerepo.v1
import googleapiclient._apis.spanner.v1
import googleapiclient._apis.speech.v1
import googleapiclient._apis.speech.v1p1beta1
import googleapiclient._apis.speech.v2beta1
import googleapiclient._apis.sqladmin.v1
import googleapiclient._apis.sqladmin.v1beta4
import googleapiclient._apis.storage.v1
import googleapiclient._apis.storagetransfer.v1
import googleapiclient._apis.streetviewpublish.v1
import googleapiclient._apis.sts.v1
import googleapiclient._apis.sts.v1beta
import googleapiclient._apis.tagmanager.v1
import googleapiclient._apis.tagmanager.v2
import googleapiclient._apis.tasks.v1
import googleapiclient._apis.testing.v1
import googleapiclient._apis.texttospeech.v1
import googleapiclient._apis.texttospeech.v1beta1
import googleapiclient._apis.toolresults.v1beta3
import googleapiclient._apis.tpu.v1
import googleapiclient._apis.tpu.v1alpha1
import googleapiclient._apis.tpu.v2
import googleapiclient._apis.tpu.v2alpha1
import googleapiclient._apis.trafficdirector.v2
import googleapiclient._apis.trafficdirector.v3
import googleapiclient._apis.transcoder.v1
import googleapiclient._apis.transcoder.v1beta1
import googleapiclient._apis.translate.v2
import googleapiclient._apis.translate.v3
import googleapiclient._apis.translate.v3beta1
import googleapiclient._apis.travelimpactmodel.v1
import googleapiclient._apis.vault.v1
import googleapiclient._apis.vectortile.v1
import googleapiclient._apis.verifiedaccess.v1
import googleapiclient._apis.verifiedaccess.v2
import googleapiclient._apis.versionhistory.v1
import googleapiclient._apis.videointelligence.v1
import googleapiclient._apis.videointelligence.v1beta2
import googleapiclient._apis.videointelligence.v1p1beta1
import googleapiclient._apis.videointelligence.v1p2beta1
import googleapiclient._apis.videointelligence.v1p3beta1
import googleapiclient._apis.vision.v1
import googleapiclient._apis.vision.v1p1beta1
import googleapiclient._apis.vision.v1p2beta1
import googleapiclient._apis.vmmigration.v1
import googleapiclient._apis.vmmigration.v1alpha1
import googleapiclient._apis.vmwareengine.v1
import googleapiclient._apis.vpcaccess.v1
import googleapiclient._apis.vpcaccess.v1beta1
import googleapiclient._apis.walletobjects.v1
import googleapiclient._apis.webfonts.v1
import googleapiclient._apis.webmasters.v3
import googleapiclient._apis.webrisk.v1
import googleapiclient._apis.websecurityscanner.v1
import googleapiclient._apis.websecurityscanner.v1alpha
import googleapiclient._apis.websecurityscanner.v1beta
import googleapiclient._apis.workflowexecutions.v1
import googleapiclient._apis.workflowexecutions.v1beta
import googleapiclient._apis.workflows.v1
import googleapiclient._apis.workflows.v1beta
import googleapiclient._apis.workloadmanager.v1
import googleapiclient._apis.workspaceevents.v1
import googleapiclient._apis.workstations.v1
import googleapiclient._apis.workstations.v1beta
import googleapiclient._apis.youtube.v3
import googleapiclient._apis.youtubeAnalytics.v1
import googleapiclient._apis.youtubeAnalytics.v2
import googleapiclient._apis.youtubereporting.v1
from googleapiclient.discovery_cache.base import Cache
from googleapiclient.http import HttpMock, HttpRequest
from googleapiclient.model import Model

_T = TypeVar("_T")

class _BytesGenerator(BytesGenerator): ...

def fix_method_name(name): ...
def key2param(key): ...

class ResourceMethodParameters:
    argmap: Incomplete

    required_params: Incomplete

    repeated_params: Incomplete

    pattern_params: Incomplete

    query_params: Incomplete

    path_params: Incomplete

    param_types: Incomplete

    enum_params: Incomplete

    def __init__(self, method_desc) -> None: ...
    def set_parameters(self, method_desc) -> None: ...

class Resource:
    def __init__(
        self,
        http,
        baseUrl,
        model,
        requestBuilder,
        developerKey,
        resourceDesc,
        rootDesc,
        schema,
    ) -> None: ...
    def __enter__(self: _T) -> _T: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        exc_tb: types.TracebackType | None,
    ) -> None: ...
    def close(self) -> None: ...

class _RequestBuilder(Protocol):
    def __call__(
        self,
        http,
        postproc,
        uri,
        method: str = ...,
        body: Incomplete | None = ...,
        headers: Incomplete | None = ...,
        methodId: Incomplete | None = ...,
        resumable: Incomplete | None = ...,
    ) -> HttpRequest: ...

@overload
def build(
    serviceName: Literal["abusiveexperiencereport"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> (
    googleapiclient._apis.abusiveexperiencereport.v1.AbusiveExperienceReportResource
): ...
@overload
def build(
    serviceName: Literal["acceleratedmobilepageurl"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> (
    googleapiclient._apis.acceleratedmobilepageurl.v1.AcceleratedmobilepageurlResource
): ...
@overload
def build(
    serviceName: Literal["accessapproval"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.accessapproval.v1.AccessApprovalResource: ...
@overload
def build(
    serviceName: Literal["accesscontextmanager"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.accesscontextmanager.v1.AccessContextManagerResource: ...
@overload
def build(
    serviceName: Literal["accesscontextmanager"],
    version: Literal["v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.accesscontextmanager.v1beta.AccessContextManagerResource: ...
@overload
def build(
    serviceName: Literal["acmedns"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.acmedns.v1.ACMEDNSResource: ...
@overload
def build(
    serviceName: Literal["addressvalidation"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.addressvalidation.v1.AddressValidationResource: ...
@overload
def build(
    serviceName: Literal["adexchangebuyer"],
    version: Literal["v1.2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.adexchangebuyer.v1_2.AdExchangeBuyerResource: ...
@overload
def build(
    serviceName: Literal["adexchangebuyer"],
    version: Literal["v1.3"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.adexchangebuyer.v1_3.AdExchangeBuyerResource: ...
@overload
def build(
    serviceName: Literal["adexchangebuyer"],
    version: Literal["v1.4"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.adexchangebuyer.v1_4.AdExchangeBuyerResource: ...
@overload
def build(
    serviceName: Literal["adexchangebuyer2"],
    version: Literal["v2beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.adexchangebuyer2.v2beta1.AdExchangeBuyerIIResource: ...
@overload
def build(
    serviceName: Literal["adexperiencereport"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.adexperiencereport.v1.AdExperienceReportResource: ...
@overload
def build(
    serviceName: Literal["admin"],
    version: Literal["datatransfer_v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.admin.datatransfer_v1.DataTransferResource: ...
@overload
def build(
    serviceName: Literal["admin"],
    version: Literal["directory_v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.admin.directory_v1.DirectoryResource: ...
@overload
def build(
    serviceName: Literal["admin"],
    version: Literal["reports_v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.admin.reports_v1.ReportsResource: ...
@overload
def build(
    serviceName: Literal["admob"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.admob.v1.AdMobResource: ...
@overload
def build(
    serviceName: Literal["admob"],
    version: Literal["v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.admob.v1beta.AdMobResource: ...
@overload
def build(
    serviceName: Literal["adsense"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.adsense.v2.AdsenseResource: ...
@overload
def build(
    serviceName: Literal["adsensehost"],
    version: Literal["v4.1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.adsensehost.v4_1.AdSenseHostResource: ...
@overload
def build(
    serviceName: Literal["adsenseplatform"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.adsenseplatform.v1.AdSensePlatformResource: ...
@overload
def build(
    serviceName: Literal["adsenseplatform"],
    version: Literal["v1alpha"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.adsenseplatform.v1alpha.AdSensePlatformResource: ...
@overload
def build(
    serviceName: Literal["advisorynotifications"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.advisorynotifications.v1.AdvisorynotificationsResource: ...
@overload
def build(
    serviceName: Literal["aiplatform"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.aiplatform.v1.AiplatformResource: ...
@overload
def build(
    serviceName: Literal["aiplatform"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.aiplatform.v1beta1.AiplatformResource: ...
@overload
def build(
    serviceName: Literal["airquality"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.airquality.v1.AirQualityResource: ...
@overload
def build(
    serviceName: Literal["alertcenter"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.alertcenter.v1beta1.AlertCenterResource: ...
@overload
def build(
    serviceName: Literal["alloydb"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.alloydb.v1.CloudAlloyDBAdminResource: ...
@overload
def build(
    serviceName: Literal["alloydb"],
    version: Literal["v1alpha"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.alloydb.v1alpha.CloudAlloyDBAdminResource: ...
@overload
def build(
    serviceName: Literal["alloydb"],
    version: Literal["v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.alloydb.v1beta.CloudAlloyDBAdminResource: ...
@overload
def build(
    serviceName: Literal["analytics"],
    version: Literal["v3"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.analytics.v3.AnalyticsResource: ...
@overload
def build(
    serviceName: Literal["analyticsadmin"],
    version: Literal["v1alpha"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.analyticsadmin.v1alpha.GoogleAnalyticsAdminResource: ...
@overload
def build(
    serviceName: Literal["analyticsadmin"],
    version: Literal["v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.analyticsadmin.v1beta.GoogleAnalyticsAdminResource: ...
@overload
def build(
    serviceName: Literal["analyticsdata"],
    version: Literal["v1alpha"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.analyticsdata.v1alpha.AnalyticsDataResource: ...
@overload
def build(
    serviceName: Literal["analyticsdata"],
    version: Literal["v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.analyticsdata.v1beta.AnalyticsDataResource: ...
@overload
def build(
    serviceName: Literal["analyticshub"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.analyticshub.v1.AnalyticsHubResource: ...
@overload
def build(
    serviceName: Literal["analyticshub"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.analyticshub.v1beta1.AnalyticsHubResource: ...
@overload
def build(
    serviceName: Literal["analyticsreporting"],
    version: Literal["v4"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.analyticsreporting.v4.AnalyticsReportingResource: ...
@overload
def build(
    serviceName: Literal["androiddeviceprovisioning"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.androiddeviceprovisioning.v1.AndroidProvisioningPartnerResource: ...
@overload
def build(
    serviceName: Literal["androidenterprise"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.androidenterprise.v1.AndroidEnterpriseResource: ...
@overload
def build(
    serviceName: Literal["androidmanagement"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.androidmanagement.v1.AndroidManagementResource: ...
@overload
def build(
    serviceName: Literal["androidpublisher"],
    version: Literal["v3"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.androidpublisher.v3.AndroidPublisherResource: ...
@overload
def build(
    serviceName: Literal["apigateway"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.apigateway.v1.ApigatewayResource: ...
@overload
def build(
    serviceName: Literal["apigateway"],
    version: Literal["v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.apigateway.v1beta.ApigatewayResource: ...
@overload
def build(
    serviceName: Literal["apigee"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.apigee.v1.ApigeeResource: ...
@overload
def build(
    serviceName: Literal["apigeeregistry"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.apigeeregistry.v1.ApigeeRegistryResource: ...
@overload
def build(
    serviceName: Literal["apikeys"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.apikeys.v2.ApiKeysServiceResource: ...
@overload
def build(
    serviceName: Literal["apim"],
    version: Literal["v1alpha"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.apim.v1alpha.APIManagementResource: ...
@overload
def build(
    serviceName: Literal["appengine"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.appengine.v1.AppengineResource: ...
@overload
def build(
    serviceName: Literal["appengine"],
    version: Literal["v1alpha"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.appengine.v1alpha.AppengineResource: ...
@overload
def build(
    serviceName: Literal["appengine"],
    version: Literal["v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.appengine.v1beta.AppengineResource: ...
@overload
def build(
    serviceName: Literal["appengine"],
    version: Literal["v1beta4"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.appengine.v1beta4.AppengineResource: ...
@overload
def build(
    serviceName: Literal["appengine"],
    version: Literal["v1beta5"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.appengine.v1beta5.AppengineResource: ...
@overload
def build(
    serviceName: Literal["apphub"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.apphub.v1.AppHubResource: ...
@overload
def build(
    serviceName: Literal["apphub"],
    version: Literal["v1alpha"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.apphub.v1alpha.AppHubResource: ...
@overload
def build(
    serviceName: Literal["area120tables"],
    version: Literal["v1alpha1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.area120tables.v1alpha1.Area120TablesResource: ...
@overload
def build(
    serviceName: Literal["areainsights"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.areainsights.v1.AreaInsightsResource: ...
@overload
def build(
    serviceName: Literal["artifactregistry"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.artifactregistry.v1.ArtifactRegistryResource: ...
@overload
def build(
    serviceName: Literal["artifactregistry"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.artifactregistry.v1beta1.ArtifactRegistryResource: ...
@overload
def build(
    serviceName: Literal["artifactregistry"],
    version: Literal["v1beta2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.artifactregistry.v1beta2.ArtifactRegistryResource: ...
@overload
def build(
    serviceName: Literal["assuredworkloads"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.assuredworkloads.v1.AssuredworkloadsResource: ...
@overload
def build(
    serviceName: Literal["assuredworkloads"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.assuredworkloads.v1beta1.AssuredworkloadsResource: ...
@overload
def build(
    serviceName: Literal["authorizedbuyersmarketplace"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.authorizedbuyersmarketplace.v1.AuthorizedBuyersMarketplaceResource: ...
@overload
def build(
    serviceName: Literal["authorizedbuyersmarketplace"],
    version: Literal["v1alpha"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.authorizedbuyersmarketplace.v1alpha.AuthorizedBuyersMarketplaceResource: ...
@overload
def build(
    serviceName: Literal["backupdr"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.backupdr.v1.BackupdrResource: ...
@overload
def build(
    serviceName: Literal["baremetalsolution"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.baremetalsolution.v1.BaremetalsolutionResource: ...
@overload
def build(
    serviceName: Literal["baremetalsolution"],
    version: Literal["v1alpha1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.baremetalsolution.v1alpha1.BaremetalsolutionResource: ...
@overload
def build(
    serviceName: Literal["baremetalsolution"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.baremetalsolution.v2.BaremetalsolutionResource: ...
@overload
def build(
    serviceName: Literal["batch"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.batch.v1.BatchResource: ...
@overload
def build(
    serviceName: Literal["beyondcorp"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.beyondcorp.v1.BeyondCorpResource: ...
@overload
def build(
    serviceName: Literal["beyondcorp"],
    version: Literal["v1alpha"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.beyondcorp.v1alpha.BeyondCorpResource: ...
@overload
def build(
    serviceName: Literal["biglake"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.biglake.v1.BigLakeServiceResource: ...
@overload
def build(
    serviceName: Literal["bigquery"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.bigquery.v2.BigqueryResource: ...
@overload
def build(
    serviceName: Literal["bigqueryconnection"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.bigqueryconnection.v1.BigQueryConnectionServiceResource: ...
@overload
def build(
    serviceName: Literal["bigqueryconnection"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> (
    googleapiclient._apis.bigqueryconnection.v1beta1.BigQueryConnectionServiceResource
): ...
@overload
def build(
    serviceName: Literal["bigquerydatapolicy"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.bigquerydatapolicy.v1.BigQueryDataPolicyServiceResource: ...
@overload
def build(
    serviceName: Literal["bigquerydatatransfer"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.bigquerydatatransfer.v1.BigQueryDataTransferResource: ...
@overload
def build(
    serviceName: Literal["bigqueryreservation"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.bigqueryreservation.v1.BigQueryReservationResource: ...
@overload
def build(
    serviceName: Literal["bigqueryreservation"],
    version: Literal["v1alpha2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.bigqueryreservation.v1alpha2.BigQueryReservationResource: ...
@overload
def build(
    serviceName: Literal["bigqueryreservation"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.bigqueryreservation.v1beta1.BigQueryReservationResource: ...
@overload
def build(
    serviceName: Literal["bigtableadmin"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.bigtableadmin.v1.BigtableAdminResource: ...
@overload
def build(
    serviceName: Literal["bigtableadmin"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.bigtableadmin.v2.BigtableAdminResource: ...
@overload
def build(
    serviceName: Literal["billingbudgets"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.billingbudgets.v1.CloudBillingBudgetResource: ...
@overload
def build(
    serviceName: Literal["billingbudgets"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.billingbudgets.v1beta1.CloudBillingBudgetResource: ...
@overload
def build(
    serviceName: Literal["binaryauthorization"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.binaryauthorization.v1.BinaryAuthorizationResource: ...
@overload
def build(
    serviceName: Literal["binaryauthorization"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.binaryauthorization.v1beta1.BinaryAuthorizationResource: ...
@overload
def build(
    serviceName: Literal["blockchainnodeengine"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.blockchainnodeengine.v1.BlockchainNodeEngineResource: ...
@overload
def build(
    serviceName: Literal["blogger"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.blogger.v2.BloggerResource: ...
@overload
def build(
    serviceName: Literal["blogger"],
    version: Literal["v3"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.blogger.v3.BloggerResource: ...
@overload
def build(
    serviceName: Literal["books"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.books.v1.BooksResource: ...
@overload
def build(
    serviceName: Literal["businessprofileperformance"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.businessprofileperformance.v1.BusinessProfilePerformanceResource: ...
@overload
def build(
    serviceName: Literal["calendar"],
    version: Literal["v3"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.calendar.v3.CalendarResource: ...
@overload
def build(
    serviceName: Literal["certificatemanager"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.certificatemanager.v1.CertificateManagerResource: ...
@overload
def build(
    serviceName: Literal["chat"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.chat.v1.HangoutsChatResource: ...
@overload
def build(
    serviceName: Literal["checks"],
    version: Literal["v1alpha"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.checks.v1alpha.ChecksServiceResource: ...
@overload
def build(
    serviceName: Literal["chromemanagement"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.chromemanagement.v1.ChromeManagementResource: ...
@overload
def build(
    serviceName: Literal["chromepolicy"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.chromepolicy.v1.ChromePolicyResource: ...
@overload
def build(
    serviceName: Literal["chromeuxreport"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.chromeuxreport.v1.ChromeUXReportResource: ...
@overload
def build(
    serviceName: Literal["civicinfo"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.civicinfo.v2.CivicInfoResource: ...
@overload
def build(
    serviceName: Literal["classroom"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.classroom.v1.ClassroomResource: ...
@overload
def build(
    serviceName: Literal["cloudasset"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudasset.v1.CloudAssetResource: ...
@overload
def build(
    serviceName: Literal["cloudasset"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudasset.v1beta1.CloudAssetResource: ...
@overload
def build(
    serviceName: Literal["cloudasset"],
    version: Literal["v1p1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudasset.v1p1beta1.CloudAssetResource: ...
@overload
def build(
    serviceName: Literal["cloudasset"],
    version: Literal["v1p4beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudasset.v1p4beta1.CloudAssetResource: ...
@overload
def build(
    serviceName: Literal["cloudasset"],
    version: Literal["v1p5beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudasset.v1p5beta1.CloudAssetResource: ...
@overload
def build(
    serviceName: Literal["cloudasset"],
    version: Literal["v1p7beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudasset.v1p7beta1.CloudAssetResource: ...
@overload
def build(
    serviceName: Literal["cloudbilling"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudbilling.v1.CloudbillingResource: ...
@overload
def build(
    serviceName: Literal["cloudbilling"],
    version: Literal["v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudbilling.v1beta.CloudbillingResource: ...
@overload
def build(
    serviceName: Literal["cloudbuild"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudbuild.v1.CloudBuildResource: ...
@overload
def build(
    serviceName: Literal["cloudbuild"],
    version: Literal["v1alpha1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudbuild.v1alpha1.CloudBuildResource: ...
@overload
def build(
    serviceName: Literal["cloudbuild"],
    version: Literal["v1alpha2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudbuild.v1alpha2.CloudBuildResource: ...
@overload
def build(
    serviceName: Literal["cloudbuild"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudbuild.v1beta1.CloudBuildResource: ...
@overload
def build(
    serviceName: Literal["cloudbuild"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudbuild.v2.CloudBuildResource: ...
@overload
def build(
    serviceName: Literal["cloudchannel"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudchannel.v1.CloudchannelResource: ...
@overload
def build(
    serviceName: Literal["cloudcommerceprocurement"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudcommerceprocurement.v1.CloudCommercePartnerProcurementServiceResource: ...
@overload
def build(
    serviceName: Literal["cloudcontrolspartner"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> (
    googleapiclient._apis.cloudcontrolspartner.v1.CloudControlsPartnerServiceResource
): ...
@overload
def build(
    serviceName: Literal["cloudcontrolspartner"],
    version: Literal["v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudcontrolspartner.v1beta.CloudControlsPartnerServiceResource: ...
@overload
def build(
    serviceName: Literal["clouddebugger"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.clouddebugger.v2.CloudDebuggerResource: ...
@overload
def build(
    serviceName: Literal["clouddeploy"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.clouddeploy.v1.CloudDeployResource: ...
@overload
def build(
    serviceName: Literal["clouderrorreporting"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.clouderrorreporting.v1beta1.ClouderrorreportingResource: ...
@overload
def build(
    serviceName: Literal["cloudfunctions"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudfunctions.v1.CloudFunctionsResource: ...
@overload
def build(
    serviceName: Literal["cloudfunctions"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudfunctions.v2.CloudFunctionsResource: ...
@overload
def build(
    serviceName: Literal["cloudfunctions"],
    version: Literal["v2alpha"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudfunctions.v2alpha.CloudFunctionsResource: ...
@overload
def build(
    serviceName: Literal["cloudfunctions"],
    version: Literal["v2beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudfunctions.v2beta.CloudFunctionsResource: ...
@overload
def build(
    serviceName: Literal["cloudidentity"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudidentity.v1.CloudIdentityResource: ...
@overload
def build(
    serviceName: Literal["cloudidentity"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudidentity.v1beta1.CloudIdentityResource: ...
@overload
def build(
    serviceName: Literal["cloudiot"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudiot.v1.CloudIotResource: ...
@overload
def build(
    serviceName: Literal["cloudkms"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudkms.v1.CloudKMSResource: ...
@overload
def build(
    serviceName: Literal["cloudprofiler"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudprofiler.v2.CloudProfilerResource: ...
@overload
def build(
    serviceName: Literal["cloudresourcemanager"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudresourcemanager.v1.CloudResourceManagerResource: ...
@overload
def build(
    serviceName: Literal["cloudresourcemanager"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> (
    googleapiclient._apis.cloudresourcemanager.v1beta1.CloudResourceManagerResource
): ...
@overload
def build(
    serviceName: Literal["cloudresourcemanager"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudresourcemanager.v2.CloudResourceManagerResource: ...
@overload
def build(
    serviceName: Literal["cloudresourcemanager"],
    version: Literal["v2beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> (
    googleapiclient._apis.cloudresourcemanager.v2beta1.CloudResourceManagerResource
): ...
@overload
def build(
    serviceName: Literal["cloudresourcemanager"],
    version: Literal["v3"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudresourcemanager.v3.CloudResourceManagerResource: ...
@overload
def build(
    serviceName: Literal["cloudscheduler"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudscheduler.v1.CloudSchedulerResource: ...
@overload
def build(
    serviceName: Literal["cloudscheduler"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudscheduler.v1beta1.CloudSchedulerResource: ...
@overload
def build(
    serviceName: Literal["cloudsearch"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudsearch.v1.CloudSearchResource: ...
@overload
def build(
    serviceName: Literal["cloudshell"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudshell.v1.CloudShellResource: ...
@overload
def build(
    serviceName: Literal["cloudshell"],
    version: Literal["v1alpha1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudshell.v1alpha1.CloudShellResource: ...
@overload
def build(
    serviceName: Literal["cloudsupport"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudsupport.v2.CloudSupportResource: ...
@overload
def build(
    serviceName: Literal["cloudsupport"],
    version: Literal["v2beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudsupport.v2beta.CloudSupportResource: ...
@overload
def build(
    serviceName: Literal["cloudtasks"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudtasks.v2.CloudTasksResource: ...
@overload
def build(
    serviceName: Literal["cloudtasks"],
    version: Literal["v2beta2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudtasks.v2beta2.CloudTasksResource: ...
@overload
def build(
    serviceName: Literal["cloudtasks"],
    version: Literal["v2beta3"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudtasks.v2beta3.CloudTasksResource: ...
@overload
def build(
    serviceName: Literal["cloudtrace"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudtrace.v1.CloudTraceResource: ...
@overload
def build(
    serviceName: Literal["cloudtrace"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudtrace.v2.CloudTraceResource: ...
@overload
def build(
    serviceName: Literal["cloudtrace"],
    version: Literal["v2beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.cloudtrace.v2beta1.CloudTraceResource: ...
@overload
def build(
    serviceName: Literal["composer"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.composer.v1.CloudComposerResource: ...
@overload
def build(
    serviceName: Literal["composer"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.composer.v1beta1.CloudComposerResource: ...
@overload
def build(
    serviceName: Literal["compute"],
    version: Literal["alpha"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.compute.alpha.ComputeResource: ...
@overload
def build(
    serviceName: Literal["compute"],
    version: Literal["beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.compute.beta.ComputeResource: ...
@overload
def build(
    serviceName: Literal["compute"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.compute.v1.ComputeResource: ...
@overload
def build(
    serviceName: Literal["config"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.config.v1.ConfigResource: ...
@overload
def build(
    serviceName: Literal["connectors"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.connectors.v1.ConnectorsResource: ...
@overload
def build(
    serviceName: Literal["connectors"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.connectors.v2.ConnectorsResource: ...
@overload
def build(
    serviceName: Literal["contactcenteraiplatform"],
    version: Literal["v1alpha1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.contactcenteraiplatform.v1alpha1.CCAIPlatformResource: ...
@overload
def build(
    serviceName: Literal["contactcenterinsights"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.contactcenterinsights.v1.ContactcenterinsightsResource: ...
@overload
def build(
    serviceName: Literal["container"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.container.v1.ContainerResource: ...
@overload
def build(
    serviceName: Literal["container"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.container.v1beta1.ContainerResource: ...
@overload
def build(
    serviceName: Literal["containeranalysis"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.containeranalysis.v1.ContainerAnalysisResource: ...
@overload
def build(
    serviceName: Literal["containeranalysis"],
    version: Literal["v1alpha1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.containeranalysis.v1alpha1.ContainerAnalysisResource: ...
@overload
def build(
    serviceName: Literal["containeranalysis"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.containeranalysis.v1beta1.ContainerAnalysisResource: ...
@overload
def build(
    serviceName: Literal["content"],
    version: Literal["v2.1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.content.v2_1.ShoppingContentResource: ...
@overload
def build(
    serviceName: Literal["content"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.content.v2.ShoppingContentResource: ...
@overload
def build(
    serviceName: Literal["contentwarehouse"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.contentwarehouse.v1.ContentwarehouseResource: ...
@overload
def build(
    serviceName: Literal["css"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.css.v1.CssResource: ...
@overload
def build(
    serviceName: Literal["customsearch"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.customsearch.v1.CustomSearchAPIResource: ...
@overload
def build(
    serviceName: Literal["datacatalog"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.datacatalog.v1.DataCatalogResource: ...
@overload
def build(
    serviceName: Literal["datacatalog"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.datacatalog.v1beta1.DataCatalogResource: ...
@overload
def build(
    serviceName: Literal["dataflow"],
    version: Literal["v1b3"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.dataflow.v1b3.DataflowResource: ...
@overload
def build(
    serviceName: Literal["dataform"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.dataform.v1beta1.DataformResource: ...
@overload
def build(
    serviceName: Literal["datafusion"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.datafusion.v1.DataFusionResource: ...
@overload
def build(
    serviceName: Literal["datafusion"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.datafusion.v1beta1.DataFusionResource: ...
@overload
def build(
    serviceName: Literal["datalabeling"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.datalabeling.v1beta1.DataLabelingResource: ...
@overload
def build(
    serviceName: Literal["datalineage"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.datalineage.v1.DatalineageResource: ...
@overload
def build(
    serviceName: Literal["datamigration"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.datamigration.v1.DatabaseMigrationServiceResource: ...
@overload
def build(
    serviceName: Literal["datamigration"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.datamigration.v1beta1.DatabaseMigrationServiceResource: ...
@overload
def build(
    serviceName: Literal["datapipelines"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.datapipelines.v1.DatapipelinesResource: ...
@overload
def build(
    serviceName: Literal["dataplex"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.dataplex.v1.CloudDataplexResource: ...
@overload
def build(
    serviceName: Literal["dataportability"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.dataportability.v1.DataPortabilityResource: ...
@overload
def build(
    serviceName: Literal["dataportability"],
    version: Literal["v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.dataportability.v1beta.DataPortabilityResource: ...
@overload
def build(
    serviceName: Literal["dataproc"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.dataproc.v1.DataprocResource: ...
@overload
def build(
    serviceName: Literal["dataproc"],
    version: Literal["v1beta2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.dataproc.v1beta2.DataprocResource: ...
@overload
def build(
    serviceName: Literal["datastore"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.datastore.v1.DatastoreResource: ...
@overload
def build(
    serviceName: Literal["datastore"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.datastore.v1beta1.DatastoreResource: ...
@overload
def build(
    serviceName: Literal["datastore"],
    version: Literal["v1beta3"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.datastore.v1beta3.DatastoreResource: ...
@overload
def build(
    serviceName: Literal["datastream"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.datastream.v1.DatastreamResource: ...
@overload
def build(
    serviceName: Literal["datastream"],
    version: Literal["v1alpha1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.datastream.v1alpha1.DatastreamResource: ...
@overload
def build(
    serviceName: Literal["deploymentmanager"],
    version: Literal["alpha"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.deploymentmanager.alpha.DeploymentManagerResource: ...
@overload
def build(
    serviceName: Literal["deploymentmanager"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.deploymentmanager.v2.DeploymentManagerResource: ...
@overload
def build(
    serviceName: Literal["deploymentmanager"],
    version: Literal["v2beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.deploymentmanager.v2beta.DeploymentManagerResource: ...
@overload
def build(
    serviceName: Literal["developerconnect"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.developerconnect.v1.DeveloperConnectResource: ...
@overload
def build(
    serviceName: Literal["dfareporting"],
    version: Literal["v3.3"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.dfareporting.v3_3.DfareportingResource: ...
@overload
def build(
    serviceName: Literal["dfareporting"],
    version: Literal["v3.4"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.dfareporting.v3_4.DfareportingResource: ...
@overload
def build(
    serviceName: Literal["dfareporting"],
    version: Literal["v3.5"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.dfareporting.v3_5.DfareportingResource: ...
@overload
def build(
    serviceName: Literal["dfareporting"],
    version: Literal["v4"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.dfareporting.v4.DfareportingResource: ...
@overload
def build(
    serviceName: Literal["dialogflow"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.dialogflow.v2.DialogflowResource: ...
@overload
def build(
    serviceName: Literal["dialogflow"],
    version: Literal["v2beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.dialogflow.v2beta1.DialogflowResource: ...
@overload
def build(
    serviceName: Literal["dialogflow"],
    version: Literal["v3"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.dialogflow.v3.DialogflowResource: ...
@overload
def build(
    serviceName: Literal["dialogflow"],
    version: Literal["v3beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.dialogflow.v3beta1.DialogflowResource: ...
@overload
def build(
    serviceName: Literal["digitalassetlinks"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.digitalassetlinks.v1.DigitalassetlinksResource: ...
@overload
def build(
    serviceName: Literal["discovery"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.discovery.v1.DiscoveryResource: ...
@overload
def build(
    serviceName: Literal["discoveryengine"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.discoveryengine.v1.DiscoveryEngineResource: ...
@overload
def build(
    serviceName: Literal["discoveryengine"],
    version: Literal["v1alpha"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.discoveryengine.v1alpha.DiscoveryEngineResource: ...
@overload
def build(
    serviceName: Literal["discoveryengine"],
    version: Literal["v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.discoveryengine.v1beta.DiscoveryEngineResource: ...
@overload
def build(
    serviceName: Literal["displayvideo"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.displayvideo.v1.DisplayVideoResource: ...
@overload
def build(
    serviceName: Literal["displayvideo"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.displayvideo.v2.DisplayVideoResource: ...
@overload
def build(
    serviceName: Literal["displayvideo"],
    version: Literal["v3"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.displayvideo.v3.DisplayVideoResource: ...
@overload
def build(
    serviceName: Literal["displayvideo"],
    version: Literal["v4"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.displayvideo.v4.DisplayVideoResource: ...
@overload
def build(
    serviceName: Literal["dlp"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.dlp.v2.DLPResource: ...
@overload
def build(
    serviceName: Literal["dns"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.dns.v1.DnsResource: ...
@overload
def build(
    serviceName: Literal["dns"],
    version: Literal["v1beta2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.dns.v1beta2.DnsResource: ...
@overload
def build(
    serviceName: Literal["dns"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.dns.v2.DnsResource: ...
@overload
def build(
    serviceName: Literal["docs"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.docs.v1.DocsResource: ...
@overload
def build(
    serviceName: Literal["documentai"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.documentai.v1.DocumentResource: ...
@overload
def build(
    serviceName: Literal["documentai"],
    version: Literal["v1beta2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.documentai.v1beta2.DocumentResource: ...
@overload
def build(
    serviceName: Literal["documentai"],
    version: Literal["v1beta3"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.documentai.v1beta3.DocumentResource: ...
@overload
def build(
    serviceName: Literal["domains"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.domains.v1.CloudDomainsResource: ...
@overload
def build(
    serviceName: Literal["domains"],
    version: Literal["v1alpha2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.domains.v1alpha2.CloudDomainsResource: ...
@overload
def build(
    serviceName: Literal["domains"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.domains.v1beta1.CloudDomainsResource: ...
@overload
def build(
    serviceName: Literal["domainsrdap"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.domainsrdap.v1.DomainsRDAPResource: ...
@overload
def build(
    serviceName: Literal["doubleclickbidmanager"],
    version: Literal["v1.1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.doubleclickbidmanager.v1_1.DoubleClickBidManagerResource: ...
@overload
def build(
    serviceName: Literal["doubleclickbidmanager"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.doubleclickbidmanager.v1.DoubleClickBidManagerResource: ...
@overload
def build(
    serviceName: Literal["doubleclickbidmanager"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.doubleclickbidmanager.v2.DoubleClickBidManagerResource: ...
@overload
def build(
    serviceName: Literal["doubleclicksearch"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.doubleclicksearch.v2.DoubleclicksearchResource: ...
@overload
def build(
    serviceName: Literal["drive"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.drive.v2.DriveResource: ...
@overload
def build(
    serviceName: Literal["drive"],
    version: Literal["v3"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.drive.v3.DriveResource: ...
@overload
def build(
    serviceName: Literal["driveactivity"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.driveactivity.v2.DriveActivityResource: ...
@overload
def build(
    serviceName: Literal["drivelabels"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.drivelabels.v2.DriveLabelsResource: ...
@overload
def build(
    serviceName: Literal["drivelabels"],
    version: Literal["v2beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.drivelabels.v2beta.DriveLabelsResource: ...
@overload
def build(
    serviceName: Literal["essentialcontacts"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.essentialcontacts.v1.EssentialcontactsResource: ...
@overload
def build(
    serviceName: Literal["eventarc"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.eventarc.v1.EventarcResource: ...
@overload
def build(
    serviceName: Literal["eventarc"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.eventarc.v1beta1.EventarcResource: ...
@overload
def build(
    serviceName: Literal["factchecktools"],
    version: Literal["v1alpha1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.factchecktools.v1alpha1.FactCheckToolsResource: ...
@overload
def build(
    serviceName: Literal["fcm"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.fcm.v1.FirebaseCloudMessagingResource: ...
@overload
def build(
    serviceName: Literal["fcmdata"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.fcmdata.v1beta1.FcmdataResource: ...
@overload
def build(
    serviceName: Literal["file"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.file.v1.CloudFilestoreResource: ...
@overload
def build(
    serviceName: Literal["file"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.file.v1beta1.CloudFilestoreResource: ...
@overload
def build(
    serviceName: Literal["firebase"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.firebase.v1beta1.FirebaseManagementResource: ...
@overload
def build(
    serviceName: Literal["firebaseappcheck"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.firebaseappcheck.v1.FirebaseappcheckResource: ...
@overload
def build(
    serviceName: Literal["firebaseappcheck"],
    version: Literal["v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.firebaseappcheck.v1beta.FirebaseappcheckResource: ...
@overload
def build(
    serviceName: Literal["firebaseappdistribution"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> (
    googleapiclient._apis.firebaseappdistribution.v1.FirebaseAppDistributionResource
): ...
@overload
def build(
    serviceName: Literal["firebaseappdistribution"],
    version: Literal["v1alpha"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.firebaseappdistribution.v1alpha.FirebaseAppDistributionResource: ...
@overload
def build(
    serviceName: Literal["firebasedatabase"],
    version: Literal["v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.firebasedatabase.v1beta.FirebaseRealtimeDatabaseResource: ...
@overload
def build(
    serviceName: Literal["firebasedataconnect"],
    version: Literal["v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.firebasedataconnect.v1beta.FirebaseDataConnectResource: ...
@overload
def build(
    serviceName: Literal["firebasedynamiclinks"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.firebasedynamiclinks.v1.FirebaseDynamicLinksResource: ...
@overload
def build(
    serviceName: Literal["firebasehosting"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.firebasehosting.v1.FirebaseHostingResource: ...
@overload
def build(
    serviceName: Literal["firebasehosting"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.firebasehosting.v1beta1.FirebaseHostingResource: ...
@overload
def build(
    serviceName: Literal["firebaseml"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.firebaseml.v1.FirebaseMLResource: ...
@overload
def build(
    serviceName: Literal["firebaseml"],
    version: Literal["v1beta2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.firebaseml.v1beta2.FirebaseMLResource: ...
@overload
def build(
    serviceName: Literal["firebaseml"],
    version: Literal["v2beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.firebaseml.v2beta.FirebaseMLResource: ...
@overload
def build(
    serviceName: Literal["firebaserules"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.firebaserules.v1.FirebaseRulesResource: ...
@overload
def build(
    serviceName: Literal["firebasestorage"],
    version: Literal["v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.firebasestorage.v1beta.FirebasestorageResource: ...
@overload
def build(
    serviceName: Literal["firestore"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.firestore.v1.FirestoreResource: ...
@overload
def build(
    serviceName: Literal["firestore"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.firestore.v1beta1.FirestoreResource: ...
@overload
def build(
    serviceName: Literal["firestore"],
    version: Literal["v1beta2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.firestore.v1beta2.FirestoreResource: ...
@overload
def build(
    serviceName: Literal["fitness"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.fitness.v1.FitnessResource: ...
@overload
def build(
    serviceName: Literal["forms"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.forms.v1.FormsResource: ...
@overload
def build(
    serviceName: Literal["games"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.games.v1.GamesResource: ...
@overload
def build(
    serviceName: Literal["gamesConfiguration"],
    version: Literal["v1configuration"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> (
    googleapiclient._apis.gamesConfiguration.v1configuration.GamesConfigurationResource
): ...
@overload
def build(
    serviceName: Literal["gameservices"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.gameservices.v1.GameServicesResource: ...
@overload
def build(
    serviceName: Literal["gameservices"],
    version: Literal["v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.gameservices.v1beta.GameServicesResource: ...
@overload
def build(
    serviceName: Literal["gamesManagement"],
    version: Literal["v1management"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.gamesManagement.v1management.GamesManagementResource: ...
@overload
def build(
    serviceName: Literal["genomics"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.genomics.v1.GenomicsResource: ...
@overload
def build(
    serviceName: Literal["genomics"],
    version: Literal["v1alpha2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.genomics.v1alpha2.GenomicsResource: ...
@overload
def build(
    serviceName: Literal["genomics"],
    version: Literal["v2alpha1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.genomics.v2alpha1.GenomicsResource: ...
@overload
def build(
    serviceName: Literal["gkebackup"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.gkebackup.v1.BackupForGKEResource: ...
@overload
def build(
    serviceName: Literal["gkehub"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.gkehub.v1.GKEHubResource: ...
@overload
def build(
    serviceName: Literal["gkehub"],
    version: Literal["v1alpha"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.gkehub.v1alpha.GKEHubResource: ...
@overload
def build(
    serviceName: Literal["gkehub"],
    version: Literal["v1alpha2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.gkehub.v1alpha2.GKEHubResource: ...
@overload
def build(
    serviceName: Literal["gkehub"],
    version: Literal["v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.gkehub.v1beta.GKEHubResource: ...
@overload
def build(
    serviceName: Literal["gkehub"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.gkehub.v1beta1.GKEHubResource: ...
@overload
def build(
    serviceName: Literal["gkehub"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.gkehub.v2.GKEHubResource: ...
@overload
def build(
    serviceName: Literal["gkehub"],
    version: Literal["v2alpha"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.gkehub.v2alpha.GKEHubResource: ...
@overload
def build(
    serviceName: Literal["gkehub"],
    version: Literal["v2beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.gkehub.v2beta.GKEHubResource: ...
@overload
def build(
    serviceName: Literal["gkeonprem"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.gkeonprem.v1.GKEOnPremResource: ...
@overload
def build(
    serviceName: Literal["gmail"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.gmail.v1.GmailResource: ...
@overload
def build(
    serviceName: Literal["gmailpostmastertools"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.gmailpostmastertools.v1.PostmasterToolsResource: ...
@overload
def build(
    serviceName: Literal["gmailpostmastertools"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.gmailpostmastertools.v1beta1.PostmasterToolsResource: ...
@overload
def build(
    serviceName: Literal["groupsmigration"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.groupsmigration.v1.GroupsMigrationResource: ...
@overload
def build(
    serviceName: Literal["groupssettings"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.groupssettings.v1.GroupssettingsResource: ...
@overload
def build(
    serviceName: Literal["healthcare"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.healthcare.v1.CloudHealthcareResource: ...
@overload
def build(
    serviceName: Literal["healthcare"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.healthcare.v1beta1.CloudHealthcareResource: ...
@overload
def build(
    serviceName: Literal["homegraph"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.homegraph.v1.HomeGraphServiceResource: ...
@overload
def build(
    serviceName: Literal["iam"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.iam.v1.IamResource: ...
@overload
def build(
    serviceName: Literal["iam"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.iam.v2.IamResource: ...
@overload
def build(
    serviceName: Literal["iam"],
    version: Literal["v2beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.iam.v2beta.IamResource: ...
@overload
def build(
    serviceName: Literal["iamcredentials"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.iamcredentials.v1.IAMCredentialsResource: ...
@overload
def build(
    serviceName: Literal["iap"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.iap.v1.CloudIAPResource: ...
@overload
def build(
    serviceName: Literal["iap"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.iap.v1beta1.CloudIAPResource: ...
@overload
def build(
    serviceName: Literal["ideahub"],
    version: Literal["v1alpha"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.ideahub.v1alpha.IdeahubResource: ...
@overload
def build(
    serviceName: Literal["ideahub"],
    version: Literal["v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.ideahub.v1beta.IdeahubResource: ...
@overload
def build(
    serviceName: Literal["identitytoolkit"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.identitytoolkit.v1.IdentityToolkitResource: ...
@overload
def build(
    serviceName: Literal["identitytoolkit"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.identitytoolkit.v2.IdentityToolkitResource: ...
@overload
def build(
    serviceName: Literal["identitytoolkit"],
    version: Literal["v3"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.identitytoolkit.v3.IdentityToolkitResource: ...
@overload
def build(
    serviceName: Literal["ids"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.ids.v1.IDSResource: ...
@overload
def build(
    serviceName: Literal["indexing"],
    version: Literal["v3"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.indexing.v3.IndexingResource: ...
@overload
def build(
    serviceName: Literal["integrations"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.integrations.v1.IntegrationsResource: ...
@overload
def build(
    serviceName: Literal["integrations"],
    version: Literal["v1alpha"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.integrations.v1alpha.IntegrationsResource: ...
@overload
def build(
    serviceName: Literal["jobs"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.jobs.v2.CloudTalentSolutionResource: ...
@overload
def build(
    serviceName: Literal["jobs"],
    version: Literal["v3"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.jobs.v3.CloudTalentSolutionResource: ...
@overload
def build(
    serviceName: Literal["jobs"],
    version: Literal["v3p1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.jobs.v3p1beta1.CloudTalentSolutionResource: ...
@overload
def build(
    serviceName: Literal["jobs"],
    version: Literal["v4"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.jobs.v4.CloudTalentSolutionResource: ...
@overload
def build(
    serviceName: Literal["keep"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.keep.v1.KeepResource: ...
@overload
def build(
    serviceName: Literal["kgsearch"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.kgsearch.v1.KgsearchResource: ...
@overload
def build(
    serviceName: Literal["kmsinventory"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.kmsinventory.v1.KmsinventoryResource: ...
@overload
def build(
    serviceName: Literal["language"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.language.v1.CloudNaturalLanguageResource: ...
@overload
def build(
    serviceName: Literal["language"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.language.v1beta1.CloudNaturalLanguageResource: ...
@overload
def build(
    serviceName: Literal["language"],
    version: Literal["v1beta2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.language.v1beta2.CloudNaturalLanguageResource: ...
@overload
def build(
    serviceName: Literal["language"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.language.v2.CloudNaturalLanguageResource: ...
@overload
def build(
    serviceName: Literal["libraryagent"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.libraryagent.v1.LibraryagentResource: ...
@overload
def build(
    serviceName: Literal["licensing"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.licensing.v1.LicensingResource: ...
@overload
def build(
    serviceName: Literal["lifesciences"],
    version: Literal["v2beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.lifesciences.v2beta.CloudLifeSciencesResource: ...
@overload
def build(
    serviceName: Literal["localservices"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.localservices.v1.LocalservicesResource: ...
@overload
def build(
    serviceName: Literal["logging"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.logging.v2.LoggingResource: ...
@overload
def build(
    serviceName: Literal["looker"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.looker.v1.LookerResource: ...
@overload
def build(
    serviceName: Literal["managedidentities"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.managedidentities.v1.ManagedServiceForMicrosoftActiveDirectoryConsumerAPIResource: ...
@overload
def build(
    serviceName: Literal["managedidentities"],
    version: Literal["v1alpha1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.managedidentities.v1alpha1.ManagedServiceForMicrosoftActiveDirectoryConsumerAPIResource: ...
@overload
def build(
    serviceName: Literal["managedidentities"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.managedidentities.v1beta1.ManagedServiceForMicrosoftActiveDirectoryConsumerAPIResource: ...
@overload
def build(
    serviceName: Literal["manufacturers"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.manufacturers.v1.ManufacturerCenterResource: ...
@overload
def build(
    serviceName: Literal["marketingplatformadmin"],
    version: Literal["v1alpha"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.marketingplatformadmin.v1alpha.GoogleMarketingPlatformAdminAPIResource: ...
@overload
def build(
    serviceName: Literal["meet"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.meet.v2.MeetResource: ...
@overload
def build(
    serviceName: Literal["memcache"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.memcache.v1.CloudMemorystoreForMemcachedResource: ...
@overload
def build(
    serviceName: Literal["memcache"],
    version: Literal["v1beta2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.memcache.v1beta2.CloudMemorystoreForMemcachedResource: ...
@overload
def build(
    serviceName: Literal["merchantapi"],
    version: Literal["accounts_v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.merchantapi.accounts_v1beta.MerchantResource: ...
@overload
def build(
    serviceName: Literal["merchantapi"],
    version: Literal["conversions_v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.merchantapi.conversions_v1beta.MerchantResource: ...
@overload
def build(
    serviceName: Literal["merchantapi"],
    version: Literal["datasources_v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.merchantapi.datasources_v1beta.MerchantResource: ...
@overload
def build(
    serviceName: Literal["merchantapi"],
    version: Literal["inventories_v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.merchantapi.inventories_v1beta.MerchantResource: ...
@overload
def build(
    serviceName: Literal["merchantapi"],
    version: Literal["lfp_v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.merchantapi.lfp_v1beta.MerchantResource: ...
@overload
def build(
    serviceName: Literal["merchantapi"],
    version: Literal["notifications_v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.merchantapi.notifications_v1beta.MerchantResource: ...
@overload
def build(
    serviceName: Literal["merchantapi"],
    version: Literal["products_v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.merchantapi.products_v1beta.MerchantResource: ...
@overload
def build(
    serviceName: Literal["merchantapi"],
    version: Literal["promotions_v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.merchantapi.promotions_v1beta.MerchantResource: ...
@overload
def build(
    serviceName: Literal["merchantapi"],
    version: Literal["quota_v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.merchantapi.quota_v1beta.MerchantResource: ...
@overload
def build(
    serviceName: Literal["merchantapi"],
    version: Literal["reports_v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.merchantapi.reports_v1beta.MerchantResource: ...
@overload
def build(
    serviceName: Literal["merchantapi"],
    version: Literal["reviews_v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.merchantapi.reviews_v1beta.MerchantResource: ...
@overload
def build(
    serviceName: Literal["metastore"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.metastore.v1.DataprocMetastoreResource: ...
@overload
def build(
    serviceName: Literal["metastore"],
    version: Literal["v1alpha"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.metastore.v1alpha.DataprocMetastoreResource: ...
@overload
def build(
    serviceName: Literal["metastore"],
    version: Literal["v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.metastore.v1beta.DataprocMetastoreResource: ...
@overload
def build(
    serviceName: Literal["metastore"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.metastore.v2.DataprocMetastoreResource: ...
@overload
def build(
    serviceName: Literal["metastore"],
    version: Literal["v2alpha"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.metastore.v2alpha.DataprocMetastoreResource: ...
@overload
def build(
    serviceName: Literal["metastore"],
    version: Literal["v2beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.metastore.v2beta.DataprocMetastoreResource: ...
@overload
def build(
    serviceName: Literal["migrationcenter"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.migrationcenter.v1.MigrationCenterAPIResource: ...
@overload
def build(
    serviceName: Literal["migrationcenter"],
    version: Literal["v1alpha1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.migrationcenter.v1alpha1.MigrationCenterAPIResource: ...
@overload
def build(
    serviceName: Literal["ml"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.ml.v1.CloudMachineLearningEngineResource: ...
@overload
def build(
    serviceName: Literal["monitoring"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.monitoring.v1.MonitoringResource: ...
@overload
def build(
    serviceName: Literal["monitoring"],
    version: Literal["v3"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.monitoring.v3.MonitoringResource: ...
@overload
def build(
    serviceName: Literal["mybusinessaccountmanagement"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.mybusinessaccountmanagement.v1.MyBusinessAccountManagementResource: ...
@overload
def build(
    serviceName: Literal["mybusinessbusinesscalls"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> (
    googleapiclient._apis.mybusinessbusinesscalls.v1.MyBusinessBusinessCallsResource
): ...
@overload
def build(
    serviceName: Literal["mybusinessbusinessinformation"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.mybusinessbusinessinformation.v1.MyBusinessBusinessInformationResource: ...
@overload
def build(
    serviceName: Literal["mybusinesslodging"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.mybusinesslodging.v1.MyBusinessLodgingResource: ...
@overload
def build(
    serviceName: Literal["mybusinessnotifications"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.mybusinessnotifications.v1.MyBusinessNotificationSettingsResource: ...
@overload
def build(
    serviceName: Literal["mybusinessplaceactions"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.mybusinessplaceactions.v1.MyBusinessPlaceActionsResource: ...
@overload
def build(
    serviceName: Literal["mybusinessqanda"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.mybusinessqanda.v1.MyBusinessQAndAResource: ...
@overload
def build(
    serviceName: Literal["mybusinessverifications"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> (
    googleapiclient._apis.mybusinessverifications.v1.MyBusinessVerificationsResource
): ...
@overload
def build(
    serviceName: Literal["netapp"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.netapp.v1.NetAppFilesResource: ...
@overload
def build(
    serviceName: Literal["netapp"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.netapp.v1beta1.NetAppFilesResource: ...
@overload
def build(
    serviceName: Literal["networkconnectivity"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.networkconnectivity.v1.NetworkconnectivityResource: ...
@overload
def build(
    serviceName: Literal["networkconnectivity"],
    version: Literal["v1alpha1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.networkconnectivity.v1alpha1.NetworkconnectivityResource: ...
@overload
def build(
    serviceName: Literal["networkmanagement"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.networkmanagement.v1.NetworkManagementResource: ...
@overload
def build(
    serviceName: Literal["networkmanagement"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.networkmanagement.v1beta1.NetworkManagementResource: ...
@overload
def build(
    serviceName: Literal["networksecurity"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.networksecurity.v1.NetworkSecurityResource: ...
@overload
def build(
    serviceName: Literal["networksecurity"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.networksecurity.v1beta1.NetworkSecurityResource: ...
@overload
def build(
    serviceName: Literal["networkservices"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.networkservices.v1.NetworkServicesResource: ...
@overload
def build(
    serviceName: Literal["networkservices"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.networkservices.v1beta1.NetworkServicesResource: ...
@overload
def build(
    serviceName: Literal["notebooks"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.notebooks.v1.AIPlatformNotebooksResource: ...
@overload
def build(
    serviceName: Literal["notebooks"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.notebooks.v2.AIPlatformNotebooksResource: ...
@overload
def build(
    serviceName: Literal["oauth2"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.oauth2.v2.Oauth2Resource: ...
@overload
def build(
    serviceName: Literal["ondemandscanning"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.ondemandscanning.v1.OnDemandScanningResource: ...
@overload
def build(
    serviceName: Literal["ondemandscanning"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.ondemandscanning.v1beta1.OnDemandScanningResource: ...
@overload
def build(
    serviceName: Literal["oracledatabase"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.oracledatabase.v1.OracleDatabaseResource: ...
@overload
def build(
    serviceName: Literal["orgpolicy"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.orgpolicy.v2.OrgPolicyAPIResource: ...
@overload
def build(
    serviceName: Literal["osconfig"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.osconfig.v1.OSConfigResource: ...
@overload
def build(
    serviceName: Literal["osconfig"],
    version: Literal["v1alpha"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.osconfig.v1alpha.OSConfigResource: ...
@overload
def build(
    serviceName: Literal["osconfig"],
    version: Literal["v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.osconfig.v1beta.OSConfigResource: ...
@overload
def build(
    serviceName: Literal["osconfig"],
    version: Literal["v2beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.osconfig.v2beta.OSConfigResource: ...
@overload
def build(
    serviceName: Literal["oslogin"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.oslogin.v1.CloudOSLoginResource: ...
@overload
def build(
    serviceName: Literal["oslogin"],
    version: Literal["v1alpha"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.oslogin.v1alpha.CloudOSLoginResource: ...
@overload
def build(
    serviceName: Literal["oslogin"],
    version: Literal["v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.oslogin.v1beta.CloudOSLoginResource: ...
@overload
def build(
    serviceName: Literal["pagespeedonline"],
    version: Literal["v5"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.pagespeedonline.v5.PagespeedInsightsResource: ...
@overload
def build(
    serviceName: Literal["parallelstore"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.parallelstore.v1.ParallelstoreResource: ...
@overload
def build(
    serviceName: Literal["parallelstore"],
    version: Literal["v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.parallelstore.v1beta.ParallelstoreResource: ...
@overload
def build(
    serviceName: Literal["paymentsresellersubscription"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.paymentsresellersubscription.v1.PaymentsResellerSubscriptionResource: ...
@overload
def build(
    serviceName: Literal["people"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.people.v1.PeopleServiceResource: ...
@overload
def build(
    serviceName: Literal["places"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.places.v1.MapsPlacesResource: ...
@overload
def build(
    serviceName: Literal["playablelocations"],
    version: Literal["v3"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.playablelocations.v3.PlayableLocationsResource: ...
@overload
def build(
    serviceName: Literal["playcustomapp"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.playcustomapp.v1.PlaycustomappResource: ...
@overload
def build(
    serviceName: Literal["playdeveloperreporting"],
    version: Literal["v1alpha1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> (
    googleapiclient._apis.playdeveloperreporting.v1alpha1.PlaydeveloperreportingResource
): ...
@overload
def build(
    serviceName: Literal["playdeveloperreporting"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> (
    googleapiclient._apis.playdeveloperreporting.v1beta1.PlaydeveloperreportingResource
): ...
@overload
def build(
    serviceName: Literal["playgrouping"],
    version: Literal["v1alpha1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.playgrouping.v1alpha1.PlayGroupingResource: ...
@overload
def build(
    serviceName: Literal["playintegrity"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.playintegrity.v1.PlayIntegrityResource: ...
@overload
def build(
    serviceName: Literal["policyanalyzer"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.policyanalyzer.v1.PolicyAnalyzerResource: ...
@overload
def build(
    serviceName: Literal["policyanalyzer"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.policyanalyzer.v1beta1.PolicyAnalyzerResource: ...
@overload
def build(
    serviceName: Literal["policysimulator"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.policysimulator.v1.PolicySimulatorResource: ...
@overload
def build(
    serviceName: Literal["policysimulator"],
    version: Literal["v1alpha"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.policysimulator.v1alpha.PolicySimulatorResource: ...
@overload
def build(
    serviceName: Literal["policysimulator"],
    version: Literal["v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.policysimulator.v1beta.PolicySimulatorResource: ...
@overload
def build(
    serviceName: Literal["policysimulator"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.policysimulator.v1beta1.PolicySimulatorResource: ...
@overload
def build(
    serviceName: Literal["policytroubleshooter"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.policytroubleshooter.v1.PolicyTroubleshooterResource: ...
@overload
def build(
    serviceName: Literal["policytroubleshooter"],
    version: Literal["v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.policytroubleshooter.v1beta.PolicyTroubleshooterResource: ...
@overload
def build(
    serviceName: Literal["pollen"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.pollen.v1.PollenResource: ...
@overload
def build(
    serviceName: Literal["poly"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.poly.v1.PolyServiceResource: ...
@overload
def build(
    serviceName: Literal["privateca"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.privateca.v1.CertificateAuthorityServiceResource: ...
@overload
def build(
    serviceName: Literal["privateca"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.privateca.v1beta1.CertificateAuthorityServiceResource: ...
@overload
def build(
    serviceName: Literal["prod_tt_sasportal"],
    version: Literal["v1alpha1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.prod_tt_sasportal.v1alpha1.SASPortalTestingResource: ...
@overload
def build(
    serviceName: Literal["publicca"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.publicca.v1.PublicCertificateAuthorityResource: ...
@overload
def build(
    serviceName: Literal["publicca"],
    version: Literal["v1alpha1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.publicca.v1alpha1.PublicCertificateAuthorityResource: ...
@overload
def build(
    serviceName: Literal["publicca"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.publicca.v1beta1.PublicCertificateAuthorityResource: ...
@overload
def build(
    serviceName: Literal["pubsub"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.pubsub.v1.PubsubResource: ...
@overload
def build(
    serviceName: Literal["pubsub"],
    version: Literal["v1beta1a"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.pubsub.v1beta1a.PubsubResource: ...
@overload
def build(
    serviceName: Literal["pubsub"],
    version: Literal["v1beta2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.pubsub.v1beta2.PubsubResource: ...
@overload
def build(
    serviceName: Literal["pubsublite"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.pubsublite.v1.PubsubLiteResource: ...
@overload
def build(
    serviceName: Literal["rapidmigrationassessment"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> (
    googleapiclient._apis.rapidmigrationassessment.v1.RapidMigrationAssessmentResource
): ...
@overload
def build(
    serviceName: Literal["readerrevenuesubscriptionlinking"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.readerrevenuesubscriptionlinking.v1.SubscriptionLinkingResource: ...
@overload
def build(
    serviceName: Literal["realtimebidding"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.realtimebidding.v1.RealTimeBiddingResource: ...
@overload
def build(
    serviceName: Literal["realtimebidding"],
    version: Literal["v1alpha"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.realtimebidding.v1alpha.RealTimeBiddingResource: ...
@overload
def build(
    serviceName: Literal["recaptchaenterprise"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.recaptchaenterprise.v1.RecaptchaEnterpriseResource: ...
@overload
def build(
    serviceName: Literal["recommendationengine"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.recommendationengine.v1beta1.RecommendationsAIResource: ...
@overload
def build(
    serviceName: Literal["recommender"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.recommender.v1.RecommenderResource: ...
@overload
def build(
    serviceName: Literal["recommender"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.recommender.v1beta1.RecommenderResource: ...
@overload
def build(
    serviceName: Literal["redis"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.redis.v1.CloudRedisResource: ...
@overload
def build(
    serviceName: Literal["redis"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.redis.v1beta1.CloudRedisResource: ...
@overload
def build(
    serviceName: Literal["remotebuildexecution"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.remotebuildexecution.v1.RemoteBuildExecutionResource: ...
@overload
def build(
    serviceName: Literal["remotebuildexecution"],
    version: Literal["v1alpha"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> (
    googleapiclient._apis.remotebuildexecution.v1alpha.RemoteBuildExecutionResource
): ...
@overload
def build(
    serviceName: Literal["remotebuildexecution"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.remotebuildexecution.v2.RemoteBuildExecutionResource: ...
@overload
def build(
    serviceName: Literal["reseller"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.reseller.v1.ResellerResource: ...
@overload
def build(
    serviceName: Literal["resourcesettings"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.resourcesettings.v1.ResourceSettingsResource: ...
@overload
def build(
    serviceName: Literal["retail"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.retail.v2.CloudRetailResource: ...
@overload
def build(
    serviceName: Literal["retail"],
    version: Literal["v2alpha"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.retail.v2alpha.CloudRetailResource: ...
@overload
def build(
    serviceName: Literal["retail"],
    version: Literal["v2beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.retail.v2beta.CloudRetailResource: ...
@overload
def build(
    serviceName: Literal["run"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.run.v1.CloudRunResource: ...
@overload
def build(
    serviceName: Literal["run"],
    version: Literal["v1alpha1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.run.v1alpha1.CloudRunResource: ...
@overload
def build(
    serviceName: Literal["run"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.run.v1beta1.CloudRunResource: ...
@overload
def build(
    serviceName: Literal["run"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.run.v2.CloudRunResource: ...
@overload
def build(
    serviceName: Literal["runtimeconfig"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.runtimeconfig.v1.CloudRuntimeConfigResource: ...
@overload
def build(
    serviceName: Literal["runtimeconfig"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.runtimeconfig.v1beta1.CloudRuntimeConfigResource: ...
@overload
def build(
    serviceName: Literal["safebrowsing"],
    version: Literal["v4"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.safebrowsing.v4.SafebrowsingResource: ...
@overload
def build(
    serviceName: Literal["safebrowsing"],
    version: Literal["v5"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.safebrowsing.v5.SafebrowsingResource: ...
@overload
def build(
    serviceName: Literal["sasportal"],
    version: Literal["v1alpha1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.sasportal.v1alpha1.SasportalResource: ...
@overload
def build(
    serviceName: Literal["script"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.script.v1.ScriptResource: ...
@overload
def build(
    serviceName: Literal["searchads360"],
    version: Literal["v0"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.searchads360.v0.SA360Resource: ...
@overload
def build(
    serviceName: Literal["searchconsole"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.searchconsole.v1.SearchConsoleResource: ...
@overload
def build(
    serviceName: Literal["secretmanager"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.secretmanager.v1.SecretManagerResource: ...
@overload
def build(
    serviceName: Literal["secretmanager"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.secretmanager.v1beta1.SecretManagerResource: ...
@overload
def build(
    serviceName: Literal["secretmanager"],
    version: Literal["v1beta2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.secretmanager.v1beta2.SecretManagerResource: ...
@overload
def build(
    serviceName: Literal["securitycenter"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.securitycenter.v1.SecurityCommandCenterResource: ...
@overload
def build(
    serviceName: Literal["securitycenter"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.securitycenter.v1beta1.SecurityCommandCenterResource: ...
@overload
def build(
    serviceName: Literal["securitycenter"],
    version: Literal["v1beta2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.securitycenter.v1beta2.SecurityCommandCenterResource: ...
@overload
def build(
    serviceName: Literal["securityposture"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.securityposture.v1.SecurityPostureResource: ...
@overload
def build(
    serviceName: Literal["serviceconsumermanagement"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> (
    googleapiclient._apis.serviceconsumermanagement.v1.ServiceConsumerManagementResource
): ...
@overload
def build(
    serviceName: Literal["serviceconsumermanagement"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.serviceconsumermanagement.v1beta1.ServiceConsumerManagementResource: ...
@overload
def build(
    serviceName: Literal["servicecontrol"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.servicecontrol.v1.ServiceControlResource: ...
@overload
def build(
    serviceName: Literal["servicecontrol"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.servicecontrol.v2.ServiceControlResource: ...
@overload
def build(
    serviceName: Literal["servicedirectory"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.servicedirectory.v1.ServiceDirectoryResource: ...
@overload
def build(
    serviceName: Literal["servicedirectory"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.servicedirectory.v1beta1.ServiceDirectoryResource: ...
@overload
def build(
    serviceName: Literal["servicemanagement"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.servicemanagement.v1.ServiceManagementResource: ...
@overload
def build(
    serviceName: Literal["servicenetworking"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.servicenetworking.v1.ServiceNetworkingResource: ...
@overload
def build(
    serviceName: Literal["servicenetworking"],
    version: Literal["v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.servicenetworking.v1beta.ServiceNetworkingResource: ...
@overload
def build(
    serviceName: Literal["serviceusage"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.serviceusage.v1.ServiceUsageResource: ...
@overload
def build(
    serviceName: Literal["serviceusage"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.serviceusage.v1beta1.ServiceUsageResource: ...
@overload
def build(
    serviceName: Literal["sheets"],
    version: Literal["v4"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.sheets.v4.SheetsResource: ...
@overload
def build(
    serviceName: Literal["siteVerification"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.siteVerification.v1.SiteVerificationResource: ...
@overload
def build(
    serviceName: Literal["slides"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.slides.v1.SlidesResource: ...
@overload
def build(
    serviceName: Literal["smartdevicemanagement"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.smartdevicemanagement.v1.SmartDeviceManagementResource: ...
@overload
def build(
    serviceName: Literal["solar"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.solar.v1.SolarResource: ...
@overload
def build(
    serviceName: Literal["sourcerepo"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.sourcerepo.v1.CloudSourceRepositoriesResource: ...
@overload
def build(
    serviceName: Literal["spanner"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.spanner.v1.SpannerResource: ...
@overload
def build(
    serviceName: Literal["speech"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.speech.v1.SpeechResource: ...
@overload
def build(
    serviceName: Literal["speech"],
    version: Literal["v1p1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.speech.v1p1beta1.SpeechResource: ...
@overload
def build(
    serviceName: Literal["speech"],
    version: Literal["v2beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.speech.v2beta1.SpeechResource: ...
@overload
def build(
    serviceName: Literal["sqladmin"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.sqladmin.v1.SQLAdminResource: ...
@overload
def build(
    serviceName: Literal["sqladmin"],
    version: Literal["v1beta4"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.sqladmin.v1beta4.SQLAdminResource: ...
@overload
def build(
    serviceName: Literal["storage"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.storage.v1.StorageResource: ...
@overload
def build(
    serviceName: Literal["storagetransfer"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.storagetransfer.v1.StoragetransferResource: ...
@overload
def build(
    serviceName: Literal["streetviewpublish"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.streetviewpublish.v1.StreetViewPublishResource: ...
@overload
def build(
    serviceName: Literal["sts"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.sts.v1.CloudSecurityTokenResource: ...
@overload
def build(
    serviceName: Literal["sts"],
    version: Literal["v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.sts.v1beta.CloudSecurityTokenResource: ...
@overload
def build(
    serviceName: Literal["tagmanager"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.tagmanager.v1.TagManagerResource: ...
@overload
def build(
    serviceName: Literal["tagmanager"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.tagmanager.v2.TagManagerResource: ...
@overload
def build(
    serviceName: Literal["tasks"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.tasks.v1.TasksResource: ...
@overload
def build(
    serviceName: Literal["testing"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.testing.v1.TestingResource: ...
@overload
def build(
    serviceName: Literal["texttospeech"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.texttospeech.v1.TexttospeechResource: ...
@overload
def build(
    serviceName: Literal["texttospeech"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.texttospeech.v1beta1.TexttospeechResource: ...
@overload
def build(
    serviceName: Literal["toolresults"],
    version: Literal["v1beta3"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.toolresults.v1beta3.ToolResultsResource: ...
@overload
def build(
    serviceName: Literal["tpu"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.tpu.v1.TPUResource: ...
@overload
def build(
    serviceName: Literal["tpu"],
    version: Literal["v1alpha1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.tpu.v1alpha1.TPUResource: ...
@overload
def build(
    serviceName: Literal["tpu"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.tpu.v2.TPUResource: ...
@overload
def build(
    serviceName: Literal["tpu"],
    version: Literal["v2alpha1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.tpu.v2alpha1.TPUResource: ...
@overload
def build(
    serviceName: Literal["trafficdirector"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.trafficdirector.v2.TrafficDirectorServiceResource: ...
@overload
def build(
    serviceName: Literal["trafficdirector"],
    version: Literal["v3"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.trafficdirector.v3.TrafficDirectorServiceResource: ...
@overload
def build(
    serviceName: Literal["transcoder"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.transcoder.v1.TranscoderResource: ...
@overload
def build(
    serviceName: Literal["transcoder"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.transcoder.v1beta1.TranscoderResource: ...
@overload
def build(
    serviceName: Literal["translate"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.translate.v2.TranslateResource: ...
@overload
def build(
    serviceName: Literal["translate"],
    version: Literal["v3"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.translate.v3.TranslateResource: ...
@overload
def build(
    serviceName: Literal["translate"],
    version: Literal["v3beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.translate.v3beta1.TranslateResource: ...
@overload
def build(
    serviceName: Literal["travelimpactmodel"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.travelimpactmodel.v1.TravelImpactModelResource: ...
@overload
def build(
    serviceName: Literal["vault"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.vault.v1.VaultResource: ...
@overload
def build(
    serviceName: Literal["vectortile"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.vectortile.v1.SemanticTileResource: ...
@overload
def build(
    serviceName: Literal["verifiedaccess"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.verifiedaccess.v1.VerifiedaccessResource: ...
@overload
def build(
    serviceName: Literal["verifiedaccess"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.verifiedaccess.v2.VerifiedaccessResource: ...
@overload
def build(
    serviceName: Literal["versionhistory"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.versionhistory.v1.VersionHistoryResource: ...
@overload
def build(
    serviceName: Literal["videointelligence"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.videointelligence.v1.CloudVideoIntelligenceResource: ...
@overload
def build(
    serviceName: Literal["videointelligence"],
    version: Literal["v1beta2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.videointelligence.v1beta2.CloudVideoIntelligenceResource: ...
@overload
def build(
    serviceName: Literal["videointelligence"],
    version: Literal["v1p1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> (
    googleapiclient._apis.videointelligence.v1p1beta1.CloudVideoIntelligenceResource
): ...
@overload
def build(
    serviceName: Literal["videointelligence"],
    version: Literal["v1p2beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> (
    googleapiclient._apis.videointelligence.v1p2beta1.CloudVideoIntelligenceResource
): ...
@overload
def build(
    serviceName: Literal["videointelligence"],
    version: Literal["v1p3beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> (
    googleapiclient._apis.videointelligence.v1p3beta1.CloudVideoIntelligenceResource
): ...
@overload
def build(
    serviceName: Literal["vision"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.vision.v1.VisionResource: ...
@overload
def build(
    serviceName: Literal["vision"],
    version: Literal["v1p1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.vision.v1p1beta1.VisionResource: ...
@overload
def build(
    serviceName: Literal["vision"],
    version: Literal["v1p2beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.vision.v1p2beta1.VisionResource: ...
@overload
def build(
    serviceName: Literal["vmmigration"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.vmmigration.v1.VMMigrationServiceResource: ...
@overload
def build(
    serviceName: Literal["vmmigration"],
    version: Literal["v1alpha1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.vmmigration.v1alpha1.VMMigrationServiceResource: ...
@overload
def build(
    serviceName: Literal["vmwareengine"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.vmwareengine.v1.VMwareEngineResource: ...
@overload
def build(
    serviceName: Literal["vpcaccess"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.vpcaccess.v1.ServerlessVPCAccessResource: ...
@overload
def build(
    serviceName: Literal["vpcaccess"],
    version: Literal["v1beta1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.vpcaccess.v1beta1.ServerlessVPCAccessResource: ...
@overload
def build(
    serviceName: Literal["walletobjects"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.walletobjects.v1.WalletobjectsResource: ...
@overload
def build(
    serviceName: Literal["webfonts"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.webfonts.v1.WebfontsResource: ...
@overload
def build(
    serviceName: Literal["webmasters"],
    version: Literal["v3"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.webmasters.v3.WebmastersResource: ...
@overload
def build(
    serviceName: Literal["webrisk"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.webrisk.v1.WebRiskResource: ...
@overload
def build(
    serviceName: Literal["websecurityscanner"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.websecurityscanner.v1.WebSecurityScannerResource: ...
@overload
def build(
    serviceName: Literal["websecurityscanner"],
    version: Literal["v1alpha"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.websecurityscanner.v1alpha.WebSecurityScannerResource: ...
@overload
def build(
    serviceName: Literal["websecurityscanner"],
    version: Literal["v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.websecurityscanner.v1beta.WebSecurityScannerResource: ...
@overload
def build(
    serviceName: Literal["workflowexecutions"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.workflowexecutions.v1.WorkflowExecutionsResource: ...
@overload
def build(
    serviceName: Literal["workflowexecutions"],
    version: Literal["v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.workflowexecutions.v1beta.WorkflowExecutionsResource: ...
@overload
def build(
    serviceName: Literal["workflows"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.workflows.v1.WorkflowsResource: ...
@overload
def build(
    serviceName: Literal["workflows"],
    version: Literal["v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.workflows.v1beta.WorkflowsResource: ...
@overload
def build(
    serviceName: Literal["workloadmanager"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.workloadmanager.v1.WorkloadManagerResource: ...
@overload
def build(
    serviceName: Literal["workspaceevents"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.workspaceevents.v1.WorkspaceEventsResource: ...
@overload
def build(
    serviceName: Literal["workstations"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.workstations.v1.CloudWorkstationsResource: ...
@overload
def build(
    serviceName: Literal["workstations"],
    version: Literal["v1beta"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.workstations.v1beta.CloudWorkstationsResource: ...
@overload
def build(
    serviceName: Literal["youtube"],
    version: Literal["v3"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.youtube.v3.YouTubeResource: ...
@overload
def build(
    serviceName: Literal["youtubeAnalytics"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.youtubeAnalytics.v1.YouTubeAnalyticsResource: ...
@overload
def build(
    serviceName: Literal["youtubeAnalytics"],
    version: Literal["v2"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.youtubeAnalytics.v2.YouTubeAnalyticsResource: ...
@overload
def build(
    serviceName: Literal["youtubereporting"],
    version: Literal["v1"],
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> googleapiclient._apis.youtubereporting.v1.YouTubeReportingResource: ...
@overload
def build(
    serviceName: str,
    version: str,
    http: httplib2.Http | HttpMock | None = None,
    discoveryServiceUrl: str | None = None,
    developerKey: str | None = None,
    model: Model | None = None,
    requestBuilder: _RequestBuilder = HttpRequest,
    credentials: oauth2client.Credentials
    | google.auth.credentials.Credentials
    | None = None,
    cache_discovery: bool = True,
    cache: Cache | None = None,
    client_options: dict[str, Any] | ClientOptions | None = None,
    adc_cert_path: str | None = None,
    adc_key_path: str | None = None,
    num_retries: int = 1,
    static_discovery: bool | None = None,
) -> Resource: ...
