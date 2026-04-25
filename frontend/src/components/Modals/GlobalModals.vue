<template>
  <CreateDocumentModal
      v-if="showCreateDocumentModal"
      v-model="showCreateDocumentModal"
      :doctype="createDocumentDoctype"
      :data="createDocumentData"
      @callback="(data) => createDocumentCallback(data)"
  />
  <QuickEntryModal
      v-if="showQuickEntryModal"
      v-model="showQuickEntryModal"
      v-bind="quickEntryProps"
  />
  <AddressModal
      v-if="showAddressModal"
      v-model="showAddressModal"
      v-bind="addressProps"
  />
  <ChangePasswordModal
      v-if="showChangePasswordModal"
      v-model="showChangePasswordModal"
  />
  <AboutModal v-model="showAboutModal" />
  <CallLogModal
      v-if="showCallLogModal"
      v-model="showCallLogModal"
      :data="callLogDataForModal"
      v-bind="callLogProps"
  />
  <PostCallSummaryModal
      v-if="showPostCallSummaryModal"
      v-model="showPostCallSummaryModal"
      :data="postCallSummaryData"
  />
</template>
<script setup>
import ChangePasswordModal from '@/components/Modals/ChangePasswordModal.vue'
import CreateDocumentModal from '@/components/Modals/CreateDocumentModal.vue'
import QuickEntryModal from '@/components/Modals/QuickEntryModal.vue'
import AddressModal from '@/components/Modals/AddressModal.vue'
import AboutModal from '@/components/Modals/AboutModal.vue'
import CallLogModal from '@/components/Modals/CallLogModal.vue'
import PostCallSummaryModal from '@/components/Modals/PostCallSummaryModal.vue'
import {
  showCreateDocumentModal,
  createDocumentDoctype,
  createDocumentData,
  createDocumentCallback,
} from '@/composables/document'
import {
  showQuickEntryModal,
  quickEntryProps,
  showAddressModal,
  addressProps,
  showAboutModal,
  showChangePasswordModal,
  showCallLogModal,
  callLogProps,
  callLogDataForModal,
} from '@/composables/modals'
</script>
