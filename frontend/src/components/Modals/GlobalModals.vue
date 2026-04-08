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
      v-bind="callLogProps"
  />
</template>
<script setup>
import ChangePasswordModal from '@/components/Modals/ChangePasswordModal.vue'
import CreateDocumentModal from '@/components/Modals/CreateDocumentModal.vue'
import QuickEntryModal from '@/components/Modals/QuickEntryModal.vue'
import AddressModal from '@/components/Modals/AddressModal.vue'
import AboutModal from '@/components/Modals/AboutModal.vue'
import CallLogModal from '@/components/Modals/CallLogModal.vue'
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
} from '@/composables/modals'
</script>
