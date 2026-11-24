import numpy as np





print("\nTABLE 1: Required sample size for AUC precision (±0.05)")
print(auc_table.to_string(index=False))

# -----------------------------------------
# TABLE 2: Sensitivity and specificity
# -----------------------------------------

performance_results = []

for confidence in [0.90, 0.95]:

    # Required positive patients for sensitivity
    n_sensitivity = find_proportion_sample_size(
        expected_value=expected_sensitivity,
        half_width=0.05,
        confidence=confidence
    )

    # Required negative patients for specificity
    n_specificity = find_proportion_sample_size(
        expected_value=expected_specificity,
        half_width=0.05,
        confidence=confidence
    )

    performance_results.append({
        "Confidence": f"{confidence:.0%}",
        "Expected sensitivity": expected_sensitivity,
        "Expected specificity": expected_specificity,
        "Positive patients (sensitivity)": n_sensitivity,
        "Negative patients (specificity)": n_specificity,
        "Total patients": n_sensitivity + n_specificity
    })

performance_table = pd.DataFrame(performance_results)

print("\nTABLE 2: Required sample size for sensitivity and specificity precision (±0.05)")
print(performance_table.to_string(index=False))